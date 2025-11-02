#!/usr/bin/env python3
"""
Test using Google's generativeai SDK directly (may bypass some SSL issues)
"""
import os
from dotenv import load_dotenv
load_dotenv()

# Try to disable SSL verification at the httplib level
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

try:
    import google.generativeai as genai
    
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    print("Testing direct Google Generative AI SDK...")
    response = model.generate_content("Say 'Hello from direct SDK!'")
    print(f"✅ Success: {response.text}")
    
except Exception as e:
    print(f"❌ Failed: {e}")
    import traceback
    traceback.print_exc()
