#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example: Create a custom podcast

This example shows how to create your own podcast with custom content.
"""

import sys
import os

# Add parent directory to path to import create_podcast module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from create_podcast import PodcastCreator, console
from rich.panel import Panel


def create_tech_podcast():
    """
    Example: Create a technology podcast
    """
    workspace_id = os.environ.get('ALIBABA_WORKSPACE_ID', 'llm-dhanwfov9gf37wez')
    
    creator = PodcastCreator(workspace_id=workspace_id)
    
    topic = "深度学习的最新进展"
    
    content = """
    深度学习作为人工智能领域的重要分支，近年来取得了突破性进展。
    
    在计算机视觉方面，Transformer架构的引入彻底改变了图像处理的范式。
    Vision Transformer (ViT) 展示了纯注意力机制在视觉任务上的强大能力，
    而CLIP模型则实现了视觉和语言的统一表示。
    
    在自然语言处理领域，大语言模型如GPT、BERT等的出现，使得机器理解
    和生成人类语言的能力达到了前所未有的高度。这些模型通过在海量文本
    数据上进行预训练，学习到了丰富的语言知识和常识。
    
    多模态学习是当前的研究热点，它能够处理和融合来自不同模态的信息，
    如文本、图像、音频和视频。这为构建更加智能和全面的AI系统奠定了基础。
    
    未来，深度学习的发展方向包括：提高模型的效率和可解释性、减少对大规模
    标注数据的依赖、增强模型的泛化能力，以及探索更加接近人类智能的学习机制。
    """
    
    console.print(Panel.fit(
        f"[bold cyan]Creating Tech Podcast[/bold cyan]\n"
        f"[yellow]Topic:[/yellow] {topic}",
        border_style="green"
    ))
    
    result = creator.submit_podcast_task(
        topic=topic,
        text=content.strip(),
        source_lang="zh-CN"
    )
    
    creator.display_result(result)
    return result


def create_story_podcast():
    """
    Example: Create a story podcast
    """
    workspace_id = os.environ.get('ALIBABA_WORKSPACE_ID', 'llm-dhanwfov9gf37wez')
    
    creator = PodcastCreator(workspace_id=workspace_id)
    
    topic = "星际旅行者的故事"
    
    content = """
    2150年，人类终于实现了星际旅行的梦想。探险号飞船载着一百名勇敢的
    探险者，向着半人马座阿尔法星系进发。
    
    飞船指挥官陈明站在观察舱，凝视着舷窗外闪烁的星空。这是人类第一次
    尝试前往太阳系之外的恒星系统，旅程将持续五年时间。
    
    "指挥官，我们检测到前方有未知信号。" 通讯官李娜的声音打断了他的
    思绪。这个信号有规律地重复着，似乎是某种智慧生命发出的。
    
    全体船员都兴奋起来。如果真的是外星文明的信号，这将是人类历史上
    最伟大的发现。他们决定改变航向，前往信号源所在的位置。
    
    经过三个月的航行，探险号接近了信号源。那是一颗蓝色的行星，被茂密的
    云层覆盖。当飞船进入轨道时，他们惊讶地发现，这颗星球上存在着高度
    发达的文明。
    
    这次相遇，开启了人类与外星文明交流的新纪元。
    """
    
    console.print(Panel.fit(
        f"[bold cyan]Creating Story Podcast[/bold cyan]\n"
        f"[yellow]Topic:[/yellow] {topic}",
        border_style="magenta"
    ))
    
    result = creator.submit_podcast_task(
        topic=topic,
        text=content.strip(),
        source_lang="zh-CN"
    )
    
    creator.display_result(result)
    return result


def create_educational_podcast():
    """
    Example: Create an educational podcast
    """
    workspace_id = os.environ.get('ALIBABA_WORKSPACE_ID', 'llm-dhanwfov9gf37wez')
    
    creator = PodcastCreator(workspace_id=workspace_id)
    
    topic = "Understanding Quantum Computing"
    
    content = """
    Quantum computing represents a paradigm shift in how we process information.
    Unlike classical computers that use bits to represent either 0 or 1, quantum
    computers use quantum bits, or qubits, which can exist in a superposition of
    both states simultaneously.
    
    This fundamental difference gives quantum computers the potential to solve
    certain problems exponentially faster than classical computers. For example,
    factoring large numbers, simulating quantum systems, and optimizing complex
    systems could become tractable with quantum computers.
    
    The principle of quantum entanglement allows qubits that are entangled to be
    correlated in ways that classical systems cannot achieve. When you measure one
    entangled qubit, you instantly know something about the other, regardless of
    the distance between them.
    
    However, quantum computing faces significant challenges. Qubits are extremely
    fragile and susceptible to environmental noise, a phenomenon known as decoherence.
    Maintaining quantum states requires operating at temperatures near absolute zero
    and isolating the system from external disturbances.
    
    Despite these challenges, major tech companies and research institutions are
    making rapid progress. We're moving from the era of quantum supremacy
    demonstrations to practical quantum advantage in specific applications.
    
    The future of quantum computing is promising, with potential applications in
    cryptography, drug discovery, artificial intelligence, and financial modeling.
    """
    
    console.print(Panel.fit(
        f"[bold cyan]Creating Educational Podcast[/bold cyan]\n"
        f"[yellow]Topic:[/yellow] {topic}",
        border_style="blue"
    ))
    
    result = creator.submit_podcast_task(
        topic=topic,
        text=content.strip(),
        source_lang="en-US"  # English content
    )
    
    creator.display_result(result)
    return result


def main():
    """
    Run all example podcasts
    """
    console.print("\n[bold]🎙️  Podcast Creation Examples[/bold]\n")
    
    console.print("[dim]Choose an example to run:[/dim]")
    console.print("1. Technology Podcast (Chinese)")
    console.print("2. Story Podcast (Chinese)")
    console.print("3. Educational Podcast (English)")
    console.print("4. Run all examples")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        create_tech_podcast()
    elif choice == "2":
        create_story_podcast()
    elif choice == "3":
        create_educational_podcast()
    elif choice == "4":
        console.print("\n[bold green]Running all examples...[/bold green]\n")
        create_tech_podcast()
        console.print("\n" + "="*60 + "\n")
        create_story_podcast()
        console.print("\n" + "="*60 + "\n")
        create_educational_podcast()
    else:
        console.print("[red]Invalid choice![/red]")
        return
    
    console.print("\n[bold green]✓ All tasks completed![/bold green]")


if __name__ == "__main__":
    main()


