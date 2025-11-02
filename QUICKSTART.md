# 🎙️ AI Podcast Creator - Ultra Quick Start

## TL;DR

```bash
# 1. Install
pip install -r requirements.txt

# 2. Run
python create_podcast.py

# Done! Your podcast task is submitted.
```

## What Just Happened?

The script submitted a podcast generation task to Alibaba Cloud. You'll get:

- **Task ID**: Track your podcast generation
- **Request ID**: For debugging
- **Log File**: Detailed logs in `log/` directory

## Next Steps

### 1. Create Your Own Podcast

Edit the `topic` and `text` in `create_podcast.py`:

```python
topic = "Your Topic Here"
text = """
Your content here...
"""
```

### 2. Try the Examples

```bash
# Simple example
python examples/simple_example.py

# Interactive menu with multiple examples
python examples/custom_podcast.py
```

### 3. Use in Your Code

```python
from create_podcast import PodcastCreator

creator = PodcastCreator(workspace_id="llm-dhanwfov9gf37wez")
result = creator.submit_podcast_task(
    topic="Hello",
    text="World",
    source_lang="en-US"
)
```

## Files Overview

```
📁 MakeYourPodcast/
├── 📄 create_podcast.py          # Main script (run this!)
├── 📄 requirements.txt            # Dependencies
├── 📄 PODCAST_README.md          # Full documentation
├── 📄 podcast.md                  # Quick start guide
├── 📄 podcast_doc.md              # API documentation
├── 📄 setup_podcast.sh            # Setup helper script
└── 📁 examples/
    ├── simple_example.py          # Minimal example
    └── custom_podcast.py          # Multiple examples
```

## Configuration

Already configured for you:

- ✅ Workspace ID: `llm-dhanwfov9gf37wez`
- ✅ Agent Key: `619d235c738a483088ac2830e69189be_p_efm`

## Languages Supported

| Code | Language |
|------|----------|
| `zh-CN` | Chinese (Simplified) |
| `en-US` | English (US) |
| `ja-JP` | Japanese |

## Help

Need more details? Check:

1. `PODCAST_README.md` - Full documentation
2. `podcast_doc.md` - API reference
3. `examples/` - Example scripts

---

**Ready? Go!**

```bash
python create_podcast.py
```


