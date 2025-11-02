#!/usr/bin/env python3
"""
Simple test script to verify podcastfy works in Docker
"""
import sys

try:
    import podcastfy
    print("✓ Podcastfy successfully imported!")
    print(f"✓ Podcastfy version: {podcastfy.__version__ if hasattr(podcastfy, '__version__') else 'unknown'}")
    
    # Try importing key modules
    from podcastfy.client import generate_podcast
    print("✓ podcastfy.client imported successfully")
    
    print("\n✅ Docker container is working correctly!")
    sys.exit(0)
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
