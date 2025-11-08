#!/usr/bin/env python3
"""
Test using Google's generativeai SDK directly (may bypass some SSL issues)
"""
import os
import certifi
from dotenv import load_dotenv
load_dotenv()

# Try to disable SSL verification at the httplib level
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
    
try:
    import os
    import google.generativeai as genai


    genai.configure(
        api_key=os.environ["GEMINI_API_KEY"],
        transport='rest',
    )

    model = genai.GenerativeModel('gemini-2.5-flash')  # Note: Model name might be 'gemini-1.5-flash'; check docs
    response = model.generate_content("What's your name?")
    print(response.text)
    
except Exception as e:
    print(f"❌ Failed: {e}")
    import traceback
    traceback.print_exc()
