#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI Podcast Creation Script
Uses Alibaba Cloud AI Podcast API to generate podcasts from text content.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.table import Table
import logging

from alibabacloud_aipodcast20250228.client import Client as AIPodcastClient
from alibabacloud_credentials.client import Client as CredentialClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_aipodcast20250228 import models as aipodcast_models
from alibabacloud_tea_util import models as util_models

from dotenv import load_dotenv
load_dotenv()

console = Console()

# Setup logging directory
log_dir = Path("log")
log_dir.mkdir(exist_ok=True)

# Create log file with timestamp
timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
log_file = log_dir / f"log_{timestamp}.log"

# Configure rich logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        RichHandler(console=console, rich_tracebacks=True),
        logging.FileHandler(log_file, encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)


class PodcastCreator:
    """
    Podcast Creator using Alibaba Cloud AI Podcast API
    """
    
    def __init__(
        self, 
        workspace_id: str,
        access_key_id: Optional[str] = None,
        access_key_secret: Optional[str] = None,
        endpoint: str = "aipodcast.cn-beijing.aliyuncs.com"
    ):
        """
        Initialize the Podcast Creator
        
        Args:
            workspace_id: Alibaba Cloud workspace ID
            access_key_id: Access Key ID (optional, can use credential chain)
            access_key_secret: Access Key Secret (optional, can use credential chain)
            endpoint: API endpoint
        """
        self.workspace_id = workspace_id
        self.endpoint = endpoint
        self.client = self._create_client(access_key_id, access_key_secret)
        
        logger.info(f"Initialized PodcastCreator with workspace: {workspace_id}")
        logger.info(f"Log file: {log_file}")
    
    def _create_client(
        self, 
        access_key_id: Optional[str] = None,
        access_key_secret: Optional[str] = None
    ) -> AIPodcastClient:
        """
        Create and configure the AI Podcast client
        
        Args:
            access_key_id: Access Key ID
            access_key_secret: Access Key Secret
            
        Returns:
            Configured AIPodcastClient instance
        """
        if access_key_id and access_key_secret:
            config = open_api_models.Config(
                access_key_id=access_key_id,
                access_key_secret=access_key_secret
            )
        else:
            # Use credential chain (environment variables, profile, etc.)
            credential = CredentialClient()
            config = open_api_models.Config(credential=credential)
        
        config.endpoint = self.endpoint
        return AIPodcastClient(config)
    
    def submit_podcast_task(
        self,
        topic: str,
        text: str,
        source_lang: str = "zh-CN"
    ) -> dict:
        """
        Submit a podcast generation task
        
        Args:
            topic: The topic/title of the podcast
            text: The content text to convert to podcast
            source_lang: Source language (default: zh-CN for Chinese)
            
        Returns:
            Response dictionary with task information
        """
        logger.info(f"Submitting podcast task: {topic}")
        
        request = aipodcast_models.PodcastTaskSubmitRequest(
            workspace_id=self.workspace_id,
            topic=topic,
            text=text,
            source_lang=source_lang
        )
        
        headers = {}
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task(description="Submitting podcast task...", total=None)
            
            response = self.client.podcast_task_submit_with_options(
                request, 
                headers, 
                util_models.RuntimeOptions()
            )
        
        # Parse response
        result = {
            "request_id": response.body.request_id if hasattr(response.body, 'request_id') else None,
            "task_id": response.body.task_id if hasattr(response.body, 'task_id') else None,
            "status": response.body.status if hasattr(response.body, 'status') else None,
            "message": response.body.message if hasattr(response.body, 'message') else None,
        }
        
        logger.info(f"Task submitted successfully. Request ID: {result.get('request_id')}")
        logger.info(f"Task ID: {result.get('task_id')}")
        
        return result
    
    def display_result(self, result: dict):
        """
        Display the task submission result in a nice format
        
        Args:
            result: Result dictionary from submit_podcast_task
        """
        table = Table(title="Podcast Task Submission Result")
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")
        
        for key, value in result.items():
            if value is not None:
                table.add_row(key.replace('_', ' ').title(), str(value))
        
        console.print(table)


def main():
    """
    Main function to create a podcast
    """
    console.print(Panel.fit(
        "[bold cyan]AI Podcast Creator[/bold cyan]\n"
        "[dim]Powered by Alibaba Cloud AI Podcast API[/dim]",
        border_style="cyan"
    ))
    
    # Get workspace ID from environment variable or use default
    workspace_id = os.environ.get('ALIBABA_WORKSPACE_ID', 'llm-dhanwfov9gf37wez')
    
    # Optional: Get access key from environment
    access_key_id = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID')
    access_key_secret = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET')
    
    # Create podcast creator
    creator = PodcastCreator(
        workspace_id=workspace_id,
        access_key_id=access_key_id,
        access_key_secret=access_key_secret
    )
    
    # Example podcast content
    topic = "AI技术在现代社会的应用与发展"
    
    text = """
    人工智能技术正在深刻改变我们的生活方式。从智能手机的语音助手，
    到自动驾驶汽车，再到医疗诊断系统，AI已经渗透到社会的各个角落。
    
    在教育领域，AI能够提供个性化的学习方案，根据每个学生的学习进度
    和特点调整教学内容。在医疗领域，AI辅助诊断系统能够帮助医生更准确
    地识别疾病，提高诊断效率。
    
    然而，AI的发展也带来了一些挑战，比如数据隐私保护、算法偏见、
    以及就业岗位的变化等问题。我们需要在享受AI带来的便利的同时，
    也要谨慎对待这些挑战，制定合理的政策和规范。
    
    未来，随着技术的不断进步，AI将在更多领域发挥重要作用。我们应该
    保持开放的态度，积极拥抱这些变化，同时也要确保技术的发展符合
    人类的价值观和伦理标准。
    """
    
    # Submit the podcast task
    console.print("\n[bold green]Submitting podcast task...[/bold green]\n")
    
    result = creator.submit_podcast_task(
        topic=topic,
        text=text.strip(),
        source_lang="zh-CN"
    )
    
    # Display the result
    creator.display_result(result)
    
    console.print(f"\n[dim]Log saved to: {log_file}[/dim]")
    console.print("[bold green]✓ Done![/bold green]")


if __name__ == "__main__":
    main()

