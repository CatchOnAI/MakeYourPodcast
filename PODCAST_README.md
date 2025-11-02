# AI Podcast Creator

This script allows you to create podcasts using the Alibaba Cloud AI Podcast API.

## Features

- 🎙️ Generate podcasts from text content
- 📝 Rich logging with timestamps
- 🎨 Beautiful console output
- 📊 Progress tracking
- 🌐 Supports multiple languages

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The script uses the following environment variables (already set in your terminal):

- `ALIBABA_WORKSPACE_ID`: Your workspace ID (default: `llm-dhanwfov9gf37wez`)
- `AGENT_KEY`: Your agent key (default: `619d235c738a483088ac2830e69189be_p_efm`)

Optional credentials (if using explicit access keys):
- `ALIBABA_CLOUD_ACCESS_KEY_ID`: Your Access Key ID
- `ALIBABA_CLOUD_ACCESS_KEY_SECRET`: Your Access Key Secret

If you don't set the explicit access keys, the SDK will use the credential chain (environment variables, profile files, etc.).

## Usage

### Basic Usage

Run the script with the example content:

```bash
python create_podcast.py
```

### Custom Usage

You can modify the script to create your own podcasts. Edit the `main()` function in `create_podcast.py`:

```python
# Example podcast content
topic = "Your Podcast Topic"
text = """
Your podcast content here...
"""

result = creator.submit_podcast_task(
    topic=topic,
    text=text,
    source_lang="zh-CN"  # or "en-US" for English
)
```

### Using as a Library

You can also import and use the `PodcastCreator` class in your own scripts:

```python
from create_podcast import PodcastCreator

# Create a podcast creator
creator = PodcastCreator(
    workspace_id="your-workspace-id"
)

# Submit a podcast task
result = creator.submit_podcast_task(
    topic="My Podcast Topic",
    text="Podcast content here...",
    source_lang="zh-CN"
)

print(f"Task ID: {result['task_id']}")
```

## Supported Languages

The `source_lang` parameter supports various languages:
- `zh-CN`: Chinese (Simplified)
- `zh-TW`: Chinese (Traditional)
- `en-US`: English (US)
- `ja-JP`: Japanese
- And more...

## Logging

All operations are logged to `log/log_YYYY_MM_DD-HH_MM_SS.log` with rich formatting.

Logs include:
- Task submission details
- Request IDs
- Task IDs
- Response status
- Any errors or warnings

## Output

The script will display:
1. A progress spinner while submitting the task
2. A formatted table with the task submission result
3. Request ID and Task ID for tracking

Example output:

```
╭─────────────────────────────────────╮
│ AI Podcast Creator                  │
│ Powered by Alibaba Cloud AI Podcast │
╰─────────────────────────────────────╯

Submitting podcast task...

┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Field        ┃ Value                          ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Request Id   │ 1234-5678-90AB-CDEF            │
│ Task Id      │ task-abc123                    │
│ Status       │ submitted                      │
└──────────────┴────────────────────────────────┘

✓ Done!
```

## API Documentation

For full API documentation, see:
- [Alibaba Cloud AI Podcast API](https://help.aliyun.com/product/AIPodcast)
- SDK Documentation in `podcast_doc.md`

## Troubleshooting

### Authentication Issues

If you encounter authentication errors, ensure:
1. Your workspace ID is correct
2. Your access credentials are properly configured
3. You have the necessary permissions

### API Endpoint Issues

If the default endpoint doesn't work, you can specify a different one:

```python
creator = PodcastCreator(
    workspace_id="your-workspace-id",
    endpoint="aipodcast.cn-shanghai.aliyuncs.com"  # Different region
)
```

## License

This project follows the same license as the main repository.


