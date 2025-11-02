#!/usr/bin/env python3
"""
Example script to generate a podcast using Docker
Make sure you have set GEMINI_API_KEY in your .env file
"""
from podcastfy.client import generate_podcast

# Example: Generate podcast from a URL
audio_file = generate_podcast(urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"])
print(f"✅ Podcast generated: {audio_file}")
