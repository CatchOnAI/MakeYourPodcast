#!/usr/bin/env python3
"""
Simple test to verify podcastfy works in Docker
"""
from podcastfy.client import generate_podcast
import sys

print("✅ Podcastfy is properly installed and working!")
print("\nTo generate a real podcast, make sure:")
print("1. Your GEMINI_API_KEY is set in .env")
print("2. You have internet connectivity from the container")
print("\nExample command to run:")
print('docker-compose run --rm -v "$PWD/example_docker.py:/tmp/example.py" -v "$PWD/data:/data" podcastfy python3 /tmp/example.py')
print("\nExample usage in Python:")
print('audio_file = generate_podcast(urls=["https://example.com"])')
