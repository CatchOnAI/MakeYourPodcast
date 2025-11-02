# MakeYourPodcast AI - Design Document

**Version:** 1.0  
**Date:** November 2, 2025  
**Status:** Architecture Documentation

---

## Executive Summary

MakeYourPodcast AI is a system that transforms user-provided topics into podcast audio through automated web research and text-to-speech generation. The system consists of two primary components:

1. **DeepResearch Agent** - An intelligent research agent that explores the web using a ReAct (Reasoning + Acting) framework to generate comprehensive reports
2. **Podcast Generation Service** - Integration with Alibaba Cloud AI Podcast API to convert text into high-quality podcast audio

**Current State:** These components exist as independent systems within the same repository and are not yet integrated into a unified pipeline.

---

## System Architecture

### High-Level Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INPUT: Research Topic                   │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   COMPONENT 1: DeepResearch Agent                │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  ReAct Loop (Think → Act → Observe)                      │   │
│  │  - Web Search (Serper API)                               │   │
│  │  - Content Extraction (Jina AI)                          │   │
│  │  - Academic Search (Google Scholar)                      │   │
│  │  - Code Execution (SandboxFusion)                        │   │
│  │  - Document Parsing (Dashscope)                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                             ▼                                    │
│              Comprehensive Research Report (Markdown)            │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              [INTEGRATION LAYER - NOT YET IMPLEMENTED]           │
│  - Content Adapter: Report → Podcast Script                     │
│  - Transcript Generation & Optimization                          │
│  - Speaker Assignment & Dialogue Structure                       │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              COMPONENT 2: Podcast Generation Service             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  PodcastCreator (Alibaba Cloud API)                      │   │
│  │  - Text-to-Speech Generation                             │   │
│  │  - Multi-language Support (CN/EN/JP)                     │   │
│  │  - Task Submission & Management                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                             ▼                                    │
│                 Task ID + Audio Generation Job                   │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│          [AUDIO RETRIEVAL - NOT YET IMPLEMENTED]                 │
│  - Task Status Polling                                           │
│  - Audio File Download                                           │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
                    FINAL PODCAST AUDIO
```

---

## Component 1: DeepResearch Agent

### Purpose
Autonomous research agent that explores the web to answer complex questions and generate comprehensive reports with citations.

### Architecture Pattern
**ReAct (Reasoning + Acting)** - An iterative loop where the agent:
1. **Think**: Reasons about the problem and plans next steps
2. **Act**: Executes tool calls to gather information
3. **Observe**: Processes tool responses
4. **Repeat**: Continues until sufficient information is gathered

### Core Components

#### 1. Agent Implementation
- **File**: `inference/react_agent_openrouter.py`
- **Class**: `MultiTurnReactAgent`
- **Key Features**:
  - Up to 100 iteration rounds
  - XML-based output parsing (`<think>`, `<tool_call>`, `<answer>`)
  - Token management and truncation
  - Error handling with retries
  - Parallel tool execution support

#### 2. Tool Suite

##### Search Tool (`tool_search.py`)
- **Provider**: Serper.dev (Google Search API)
- **Function**: Batch web searches
- **Input**: List of search queries
- **Output**: Top 10 results per query with titles, URLs, snippets
- **Use Case**: Initial topic exploration, finding relevant sources

##### Visit Tool (`tool_visit.py`)
- **Providers**: 
  - Jina AI (content extraction)
  - OpenRouter (summarization)
- **Function**: Read and summarize webpage content
- **Input**: List of URLs
- **Output**: Extracted text + AI-generated summary
- **Features**: 
  - Automatic retry logic
  - Content truncation (40K chars)
  - Chinese content detection
  - Multiple URL processing

##### Scholar Tool (`tool_scholar.py`)
- **Provider**: Serper.dev (Google Scholar API)
- **Function**: Academic paper search
- **Input**: Research queries
- **Output**: Paper citations, abstracts, publication info
- **Use Case**: Academic research, scientific topics

##### PythonInterpreter Tool (`tool_python.py`)
- **Provider**: SandboxFusion API
- **Function**: Execute Python code in isolated sandbox
- **Input**: Python code string
- **Output**: Execution results (stdout, stderr, files)
- **Use Case**: Data analysis, calculations, visualizations

##### FileParser Tool (`tool_file.py`)
- **Provider**: Dashscope (Alibaba Document Parser)
- **Function**: Parse documents and multimedia files
- **Supported Formats**: PDF, DOCX, XLSX, PPT, images, videos
- **Features**: OCR, table extraction, multimodal analysis
- **Use Case**: Document analysis, research paper processing

#### 3. LLM Integration

**Primary Model**: Tongyi-DeepResearch-30B-A3B
- **Architecture**: Mixture-of-Experts (MoE), 30B parameters
- **Provider**: OpenRouter API
- **Model ID**: `alibaba/tongyi-deepresearch-30b-a3b`
- **Capabilities**: 
  - Advanced reasoning
  - Tool use
  - Long context (128K tokens)
  - Multilingual (Chinese/English)

**Summarization Model Options**:
- `alibaba/qwen-max`
- `gpt-4o-mini`
- Configurable via `SUMMARY_MODEL_NAME`

### Data Flow

```
User Question: "Explain quantum entanglement"
    ↓
[Round 1-3] Initial Planning
    <think>Need to explain basic concept, history, applications</think>
    ↓
[Round 4-10] Information Gathering
    <tool_call>{"name": "search", "arguments": {"query": ["quantum entanglement basics"]}}</tool_call>
    <tool_response>[Search results with 10 links]</tool_response>
    <tool_call>{"name": "visit", "arguments": {"url": ["wikipedia.org/...", "nature.com/..."]}}</tool_call>
    <tool_response>[Extracted content + summaries]</tool_response>
    ↓
[Round 11-20] Deep Research
    <tool_call>{"name": "google_scholar", "arguments": {"query": ["EPR paradox Bell theorem"]}}</tool_call>
    <tool_response>[Academic papers with citations]</tool_response>
    ↓
[Round 21-30] Synthesis
    <think>Have enough information. Need to structure: definition, history, theory, applications</think>
    ↓
[Final] Answer Generation
    <answer>
    # Quantum Entanglement: A Comprehensive Overview
    
    Quantum entanglement is a phenomenon where particles become correlated...
    [Comprehensive markdown report with citations]
    </answer>
```

### Output Formats

1. **Full JSON** (`*_full.json`)
   - Complete conversation history
   - All tool calls and responses
   - Thinking traces
   - Metadata (tokens, rounds, execution time)

2. **Readable Markdown** (`*_readable.md`)
   - Formatted answer
   - Research methodology summary
   - Source citations
   - Human-friendly report structure

### Configuration Requirements

```bash
# Core LLM
OPENROUTER_API_KEY=<key>

# Web Search
SERPER_KEY_ID=<key>

# Web Content Extraction
JINA_API_KEYS=<key>

# Summarization
SUMMARY_MODEL_NAME=alibaba/tongyi-deepresearch-30b-a3b

# Optional: Advanced Features
DASHSCOPE_API_KEY=<key>           # Document parsing
SANDBOX_FUSION_ENDPOINT=<url>      # Code execution
```

### Key Files
- **Agent**: `inference/react_agent_openrouter.py`
- **Runner**: `inference/run_openrouter.py`
- **Tools**: `inference/tool_*.py`
- **Prompts**: `inference/prompt.py`
- **Documentation**: `inference/README_OPENROUTER.md`, `inference/START_HERE.md`

---

## Component 2: Podcast Generation Service

### Purpose
Convert text content into high-quality podcast audio using Alibaba Cloud AI Podcast API.

### Architecture Pattern
**Simple API Wrapper** - Client-server pattern with cloud-based text-to-speech generation.

### Core Components

#### PodcastCreator Class
- **File**: `create_podcast.py`
- **Responsibilities**:
  - Initialize Alibaba Cloud SDK client
  - Configure authentication
  - Submit podcast generation tasks
  - Display task results

### API Integration

#### Request Flow
```python
PodcastTaskSubmitRequest(
    topic="Research Topic Title",        # Podcast title
    text="Full content text...",         # Content to convert
    source_lang="en-US"                  # Language code
)
    ↓
Submit to: aipodcast.cn-beijing.aliyuncs.com
    ↓
Response:
    - task_id: Unique task identifier
    - request_id: API request tracking ID
```

#### Supported Languages
- **Chinese**: `zh-CN` (Simplified), `zh-TW` (Traditional)
- **English**: `en-US`
- **Japanese**: `ja-JP`

### Configuration Requirements

```bash
# Alibaba Cloud Credentials
ALIBABA_WORKSPACE_ID=<workspace_id>
ALIBABA_CLOUD_ACCESS_KEY_ID=<access_key>
ALIBABA_CLOUD_ACCESS_KEY_SECRET=<secret_key>
```

### Current Limitations

1. **No Audio Retrieval**: System only submits tasks, doesn't retrieve generated audio files
2. **No Status Polling**: Cannot check if podcast generation is complete
3. **No Error Handling**: Limited feedback on generation failures
4. **No Download Mechanism**: Missing code to fetch final audio files

### Key Files
- **Main**: `create_podcast.py`
- **Examples**: `examples/custom_podcast.py`
- **Documentation**: `PODCAST_README.md`, `podcast.md`

---

## Integration Architecture (Proposed)

### Missing Components

The following components are **not yet implemented** but are necessary for a complete pipeline:

#### 1. Content Adapter
**Purpose**: Transform research reports into podcast-optimized scripts

**Requirements**:
- Parse markdown research output
- Extract key findings and structure
- Generate conversational narrative
- Optimize length for audio (target: 10-30 minutes)
- Add transitions and pacing

**Proposed Implementation**:
```python
class ContentAdapter:
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def transform_report_to_script(self, research_report: str) -> str:
        """Convert research report to podcast transcript"""
        prompt = f"""
        Convert this research report into a natural podcast script:
        - Use conversational tone
        - Add engaging transitions
        - Target length: 2000-5000 words
        - Maintain key facts and citations
        
        Report:
        {research_report}
        """
        return self.llm.generate(prompt)
```

#### 2. Task Management System
**Purpose**: Poll Alibaba Cloud API for task completion and retrieve audio

**Requirements**:
- Poll task status endpoint
- Wait for completion (with timeout)
- Download generated audio file
- Handle errors and retries

**Proposed Implementation**:
```python
class PodcastTaskManager:
    def poll_task_status(self, task_id: str) -> str:
        """Check task status until complete"""
        # Poll API endpoint (needs documentation)
        pass
    
    def download_audio(self, task_id: str, output_path: str):
        """Retrieve generated podcast audio"""
        # Download from cloud storage (needs documentation)
        pass
```

#### 3. Unified CLI
**Purpose**: Single command to run complete pipeline

**Proposed Interface**:
```bash
# Simple usage
python main.py "Explain quantum computing" --output podcast.mp3

# Advanced options
python main.py "Climate change impacts" \
    --lang en-US \
    --research-depth comprehensive \
    --podcast-style conversational \
    --max-length 20min
```

### Proposed End-to-End Flow

```python
# main.py (unified pipeline)
class PodcastPipeline:
    def __init__(self):
        self.research_agent = MultiTurnReactAgent()
        self.content_adapter = ContentAdapter()
        self.podcast_creator = PodcastCreator()
        self.task_manager = PodcastTaskManager()
    
    def generate_podcast(self, topic: str, lang: str = "en-US") -> str:
        # Step 1: Research
        print(f"Researching: {topic}")
        research_report = self.research_agent.run(topic)
        
        # Step 2: Transform to script
        print("Generating podcast script...")
        script = self.content_adapter.transform_report_to_script(
            research_report
        )
        
        # Step 3: Generate audio
        print("Creating podcast audio...")
        task_id = self.podcast_creator.submit_podcast_task(
            topic=topic,
            text=script,
            source_lang=lang
        )
        
        # Step 4: Wait and download
        print(f"Waiting for generation (Task: {task_id})...")
        self.task_manager.poll_task_status(task_id)
        
        output_path = f"output/{topic.replace(' ', '_')}.mp3"
        self.task_manager.download_audio(task_id, output_path)
        
        print(f"Podcast saved to: {output_path}")
        return output_path
```

---

## Technical Specifications

### Dependencies

#### DeepResearch Component
```
openai>=1.0.0                  # OpenRouter client
qwen-agent>=0.0.26            # Agent framework
requests>=2.32.0              # HTTP client
aiohttp==3.12.15              # Async HTTP
rich>=14.0.0                  # Console UI
tiktoken>=0.6.0               # Token counting
sandbox-fusion>=0.3.0         # Code execution
pandas>=2.0.0                 # Data analysis
pdfplumber>=0.11.0            # PDF parsing
python-pptx>=1.0.0            # PPT parsing
openpyxl>=3.1.0               # Excel parsing
```

#### Podcast Component
```
rich==13.7.0                              # Console UI
alibabacloud_aipodcast20250228==1.0.4     # Podcast API
alibabacloud_credentials>=0.3.0           # Authentication
alibabacloud_tea_openapi>=0.3.0           # API client
alibabacloud_tea_util>=0.3.0              # Utilities
```

### API Requirements

| Service | Provider | Purpose | Required |
|---------|----------|---------|----------|
| LLM | OpenRouter | Agent reasoning & summarization | Yes |
| Search | Serper.dev | Web search | Yes |
| Content Extraction | Jina AI | Webpage reading | Yes |
| Podcast Generation | Alibaba Cloud | Text-to-speech | Yes |
| Code Execution | SandboxFusion | Python interpreter | Optional |
| Document Parsing | Dashscope | File analysis | Optional |

### Performance Characteristics

#### Research Agent
- **Average execution time**: 2-5 minutes for comprehensive research
- **API calls**: 10-30 per research session
- **Cost estimate**: $0.10-$0.50 per research (depending on depth)
- **Output size**: 2K-10K words

#### Podcast Generation
- **Processing time**: 1-3 minutes (server-side)
- **Cost**: Based on Alibaba Cloud pricing
- **Output format**: MP3 audio file
- **Quality**: High-quality AI voice

---

## Deployment Options

### Option 1: Fully Cloud-Based (Recommended)
**Setup:**
- DeepResearch: OpenRouter API
- Podcast: Alibaba Cloud API
- All tools: Cloud APIs

**Advantages:**
- No local GPU required
- Scalable
- Easy deployment

**Disadvantages:**
- API costs
- Internet dependency

### Option 2: Hybrid (Local Research)
**Setup:**
- DeepResearch: Local Tongyi-DeepResearch-30B model
- Podcast: Alibaba Cloud API

**Advantages:**
- Lower API costs for research
- More control over research agent

**Disadvantages:**
- Requires GPU (24GB+ VRAM)
- Complex local setup

### Option 3: Development Mode
**Setup:**
- Research only (no podcast generation)
- Use for testing and development

**Configuration:**
```bash
# Run research only
python inference/run_openrouter.py "Your topic"

# Run podcast generation only (with pre-written text)
python create_podcast.py
```

---

## Error Handling & Resilience

### Research Agent
- **Tool failures**: Automatic retry with exponential backoff
- **Token limits**: Content truncation and summarization
- **API rate limits**: Request queuing and throttling
- **Network errors**: Retry logic with timeout

### Podcast Generation
- **Task submission failures**: Retry with error logging
- **Invalid credentials**: Clear error messages
- **Language support**: Validation before submission

### Proposed Integration Layer
- **Pipeline failures**: Save intermediate results (research, script)
- **Checkpoint system**: Resume from last successful stage
- **Fallback options**: Alternative TTS services if Alibaba Cloud fails

---

## Security Considerations

### API Key Management
- All keys stored in `.env` file (not committed to git)
- Environment variable validation on startup
- Secure credential storage using `alibabacloud_credentials`

### Data Privacy
- Research data: Processed via third-party APIs (OpenRouter, Jina, Serper)
- Podcast content: Sent to Alibaba Cloud servers
- No local data storage of sensitive information

### Recommendations
1. Use separate API keys for development and production
2. Implement rate limiting to prevent quota exhaustion
3. Add audit logging for API calls
4. Consider data encryption for sensitive research topics

---

## Extension Points

### Future Enhancements

#### 1. Multi-Speaker Podcasts
- Generate dialogue between multiple speakers
- Assign different voices to hosts/guests
- Add natural conversation dynamics

#### 2. Content Optimization
- Automatic length adjustment
- Difficulty level selection (beginner, intermediate, expert)
- Style customization (educational, storytelling, interview)

#### 3. Audio Post-Processing
- Background music integration
- Sound effects
- Audio editing and mixing
- Intro/outro generation

#### 4. Alternative TTS Services
- OpenAI TTS API
- ElevenLabs
- Azure Speech Services
- Local TTS models (Coqui, Bark)

#### 5. Caching & Optimization
- Cache research results for similar topics
- Reuse tool responses
- Batch processing for multiple podcasts

#### 6. Quality Assurance
- Fact-checking layer
- Citation verification
- Script review before audio generation
- A/B testing for different script styles

---

## Development Roadmap

### Phase 1: Integration (Current Priority)
- [ ] Implement audio retrieval from Alibaba Cloud
- [ ] Add task status polling
- [ ] Create content adapter (report → script)
- [ ] Build unified CLI

### Phase 2: Enhancement
- [ ] Add multi-speaker support
- [ ] Implement caching system
- [ ] Create web UI for easier access
- [ ] Add progress tracking dashboard

### Phase 3: Production
- [ ] Deployment automation
- [ ] Monitoring and logging
- [ ] API rate limit management
- [ ] Cost optimization
- [ ] Documentation website

---

## Known Issues & Limitations

### Current Limitations

1. **No Integration**: Research and podcast systems are separate
2. **No Audio Retrieval**: Cannot download generated podcasts
3. **No Status Tracking**: Cannot monitor podcast generation progress
4. **Single Language Per Session**: Cannot mix languages in one podcast
5. **No Length Control**: Research reports may be too long for audio
6. **Limited Error Recovery**: Pipeline failures require manual intervention

### Workarounds

1. **Manual Integration**: 
   - Run research agent separately
   - Copy output to text file
   - Manually edit for podcast format
   - Run podcast generator with edited text

2. **Task Tracking**:
   - Save task IDs manually
   - Check Alibaba Cloud console for status

---

## Conclusion

MakeYourPodcast AI demonstrates a solid foundation with two powerful components:
- **DeepResearch Agent**: State-of-the-art autonomous research with tool use
- **Podcast Generator**: High-quality text-to-speech via cloud API

The primary development opportunity is creating the integration layer to connect these systems into a seamless pipeline. With the proposed content adapter, task management system, and unified CLI, this project can deliver on its promise of fully automated podcast generation from any research topic.

### Success Metrics
- **Research Quality**: Comprehensive, accurate, well-cited reports
- **Audio Quality**: Natural-sounding, engaging podcast audio
- **User Experience**: Single command from topic to podcast
- **Performance**: End-to-end generation in under 10 minutes
- **Cost Efficiency**: Under $1 per podcast episode

---

## Appendices

### A. Example Usage

#### Current (Separate Systems)
```bash
# Step 1: Research
cd inference
python run_openrouter.py "History of artificial intelligence"
# Output: ai_history_readable.md

# Step 2: Manual editing
# Edit the markdown file to create podcast script

# Step 3: Generate podcast
cd ..
python create_podcast.py
# Input script manually when prompted
```

#### Proposed (Integrated)
```bash
# Single command
python main.py "History of artificial intelligence" \
    --lang en-US \
    --output ai_history_podcast.mp3

# Output: 
# - ai_history_research.md (research report)
# - ai_history_script.txt (podcast script)
# - ai_history_podcast.mp3 (final audio)
```

### B. Configuration Examples

#### Minimal Setup (Cloud Only)
```bash
# .env
OPENROUTER_API_KEY=sk-or-v1-...
SERPER_KEY_ID=...
JINA_API_KEYS=jina_...
ALIBABA_WORKSPACE_ID=...
ALIBABA_CLOUD_ACCESS_KEY_ID=...
ALIBABA_CLOUD_ACCESS_KEY_SECRET=...
SUMMARY_MODEL_NAME=alibaba/tongyi-deepresearch-30b-a3b
```

#### Advanced Setup (All Features)
```bash
# .env (with optional features)
OPENROUTER_API_KEY=sk-or-v1-...
SERPER_KEY_ID=...
JINA_API_KEYS=jina_...
ALIBABA_WORKSPACE_ID=...
ALIBABA_CLOUD_ACCESS_KEY_ID=...
ALIBABA_CLOUD_ACCESS_KEY_SECRET=...
SUMMARY_MODEL_NAME=alibaba/tongyi-deepresearch-30b-a3b
DASHSCOPE_API_KEY=...           # For document parsing
SANDBOX_FUSION_ENDPOINT=...      # For code execution
AGENT_KEY=...                    # For qwen-agent features
```

### C. File Structure Reference

```
MakeYourPodcast/
├── main.py                      # [Future] Unified entry point
├── create_podcast.py            # Podcast generation
├── requirements.txt             # Python dependencies
├── .env                         # API credentials
├── DESIGN_DOC.md               # This document
├── README.md                    # Project overview
│
├── inference/                   # DeepResearch component
│   ├── react_agent_openrouter.py    # Main agent
│   ├── run_openrouter.py            # Runner script
│   ├── prompt.py                    # System prompts
│   ├── tool_search.py               # Web search
│   ├── tool_visit.py                # Content extraction
│   ├── tool_scholar.py              # Academic search
│   ├── tool_python.py               # Code execution
│   ├── tool_file.py                 # Document parsing
│   └── README_OPENROUTER.md         # Documentation
│
├── examples/                    # Usage examples
│   └── custom_podcast.py
│
└── evaluation/                  # Testing & evaluation
    ├── evaluate_deepsearch_official.py
    └── eval_data/
```

### D. API Endpoints Reference

| Service | Endpoint | Documentation |
|---------|----------|---------------|
| OpenRouter | `https://openrouter.ai/api/v1` | openrouter.ai/docs |
| Serper Search | `https://google.serper.dev/search` | serper.dev/docs |
| Jina AI | `https://r.jina.ai/` | jina.ai/docs |
| Alibaba Podcast | `aipodcast.cn-beijing.aliyuncs.com` | Alibaba Cloud Console |

---

**Document End**
