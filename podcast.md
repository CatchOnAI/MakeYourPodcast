# AI Podcast Creation - Quick Start

## 🎙️ What You Have

A complete Python script to create podcasts using Alibaba Cloud's AI Podcast API!

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or use the setup script:

```bash
bash setup_podcast.sh
```

### Step 2: Run Your First Podcast

```bash
python create_podcast.py
```

This will create a podcast about AI technology (in Chinese).

### Step 3: Create Your Own Podcast

Edit `create_podcast.py` or use the examples:

```bash
# Simple example
python examples/simple_example.py

# Multiple examples with menu
python examples/custom_podcast.py
```

## 📝 Create Custom Podcasts

```python
from create_podcast import PodcastCreator

# Initialize
creator = PodcastCreator(workspace_id="your-workspace-id")

# Create podcast
result = creator.submit_podcast_task(
    topic="My Amazing Topic",
    text="Your podcast content here...",
    source_lang="zh-CN"  # or "en-US" for English
)

print(f"Task ID: {result['task_id']}")
```

## 🌐 Supported Languages

- `zh-CN` - Chinese (Simplified)
- `en-US` - English
- `ja-JP` - Japanese
- And more...

## 📊 What You Get

- ✅ Task ID for tracking your podcast
- ✅ Request ID for API debugging
- ✅ Rich console output with progress tracking
- ✅ Detailed logs in `log/log_YYYY_MM_DD-HH_MM_SS.log`

## 🔧 Configuration

Your credentials are already configured:
- Workspace ID: `llm-dhanwfov9gf37wez`
- Agent Key: `619d235c738a483088ac2830e69189be_p_efm`

## 📚 More Information

- Full documentation: `PODCAST_README.md`
- API documentation: `podcast_doc.md`
- Example scripts: `examples/` directory

## 🎯 Key Features

1. **Easy to Use**: Simple API with sensible defaults
2. **Rich Logging**: Beautiful console output + file logs
3. **Multiple Examples**: Tech, story, and educational podcasts
4. **Language Support**: Chinese and English (and more)
5. **Production Ready**: Follows best practices (no bare try-except, rich logging)

## 💡 Example Use Cases

1. **Content Creation**: Convert blog posts to podcasts
2. **Education**: Create audio lessons from text
3. **Storytelling**: Turn stories into audio format
4. **News**: Generate news podcasts automatically
5. **Documentation**: Create audio documentation

---

**Ready to create your first podcast? Run:**

```bash
python create_podcast.py
```

🎉 Happy podcasting!


