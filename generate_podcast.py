#!/usr/bin/env python3
"""
Simple example to generate a podcast
"""
import os
import sys
import certifi

# Fix SSL certificate issues on macOS - must be set before any imports
cert_path = certifi.where()
os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = cert_path
os.environ['SSL_CERT_FILE'] = cert_path
os.environ['REQUESTS_CA_BUNDLE'] = cert_path
os.environ['CURL_CA_BUNDLE'] = cert_path

# Additional gRPC SSL settings
os.environ['GRPC_VERBOSITY'] = 'ERROR'  # Reduce gRPC logging
os.environ['GRPC_TRACE'] = ''

from podcastfy.client import generate_podcast

print("🎙️ Generating podcast from Wikipedia article...")
audio_file = generate_podcast(
    urls=["/Users/dingkwang/MakeYourPodcast/podcastfy-main/paper/paper.pdf"],
    tts_model="openai"  # or "edge" for free TTS
)
print(f"✅ Podcast generated: {audio_file}")
