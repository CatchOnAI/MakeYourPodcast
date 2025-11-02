#!/usr/bin/env python3
"""
Simple example to generate a podcast
"""
import os
import sys
import certifi
import ssl

# Fix SSL certificate issues on macOS - must be set before any imports
cert_path = certifi.where()
os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = cert_path
os.environ['SSL_CERT_FILE'] = cert_path
os.environ['REQUESTS_CA_BUNDLE'] = cert_path
os.environ['CURL_CA_BUNDLE'] = cert_path

# Additional gRPC SSL settings
os.environ['GRPC_VERBOSITY'] = 'ERROR'  # Reduce gRPC logging
os.environ['GRPC_TRACE'] = ''

# Disable SSL verification as fallback (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

from podcastfy.client import generate_podcast

print("🎙️ Generating podcast from Wikipedia article...")

# Configure conversation settings with timeout
conversation_config = {
    "conversation_style": ["engaging", "fast-paced"],
    "roles_person1": "main summarizer",
    "roles_person2": "questioner",
    "dialogue_structure": ["Introduction", "Main Content Summary", "Conclusion"],
    "podcast_name": "Research Paper Podcast",
    "creativity": 0.7,
    "api_timeout": 60,  # 60 second timeout
}

# LLM config with timeout
llm_config = {
    "timeout": 60,  # 60 second timeout for API calls
}

try:
    audio_file = generate_podcast(
        urls=["/Users/dingkwang/MakeYourPodcast/podcastfy-main/paper/paper.pdf"],
        tts_model="edge",  # Using free edge TTS to avoid OpenAI API costs
        conversation_config=conversation_config,
        longform=False,  # Shorter podcast for testing
        llm_config=llm_config
    )
    print(f"✅ Podcast generated: {audio_file}")
except Exception as e:
    print(f"❌ Error generating podcast: {e}")
    import traceback
    traceback.print_exc()
