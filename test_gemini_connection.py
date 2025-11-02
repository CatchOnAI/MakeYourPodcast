#!/usr/bin/env python3
"""
Test script to verify ChatGoogleGenerativeAI connection
"""
import os
import sys
import ssl
import certifi
import urllib3

from dotenv import load_dotenv
load_dotenv()

# Disable SSL warnings for testing (not recommended for production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Fix SSL certificate issues on macOS
cert_path = certifi.where()
os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = cert_path
os.environ['SSL_CERT_FILE'] = cert_path
os.environ['REQUESTS_CA_BUNDLE'] = cert_path
os.environ['CURL_CA_BUNDLE'] = cert_path

# Disable SSL verification as workaround for corporate SSL issues
ssl._create_default_https_context = ssl._create_unverified_context

from langchain_google_genai import ChatGoogleGenerativeAI

def test_rest_api():
    """Test using REST API (no gRPC SSL issues)"""
    print("Testing ChatGoogleGenerativeAI with REST transport...")
    try:
        llm = ChatGoogleGenerativeAI(
            api_key=os.environ["GEMINI_API_KEY"],
            model="gemini-1.5-flash",
            max_output_tokens=100,
            timeout=60,
            transport="rest",  # Use REST instead of gRPC
            temperature=0.7,
        )
        
        response = llm.invoke("Say 'Hello, REST API works!'")
        print(f"✅ REST API Success: {response.content}")
        return True
    except Exception as e:
        print(f"❌ REST API Failed: {e}")
        return False

def test_grpc_api():
    """Test using gRPC API (may have SSL issues)"""
    print("\nTesting ChatGoogleGenerativeAI with gRPC transport...")
    try:
        llm = ChatGoogleGenerativeAI(
            api_key=os.environ["GEMINI_API_KEY"],
            model="gemini-1.5-flash",
            max_output_tokens=100,
            timeout=60,
            temperature=0.7,
        )
        
        response = llm.invoke("Say 'Hello, gRPC works!'")
        print(f"✅ gRPC Success: {response.content}")
        return True
    except Exception as e:
        print(f"❌ gRPC Failed: {e}")
        return False

if __name__ == "__main__":
    # Check if API key is set
    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ GEMINI_API_KEY not found in environment")
        sys.exit(1)
    
    print("=" * 60)
    print("Testing Gemini API Connection")
    print("=" * 60)
    
    # Test REST first (should work)
    rest_works = test_rest_api()
    
    # Test gRPC (might fail with SSL issues)
    grpc_works = test_grpc_api()
    
    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  REST API: {'✅ Working' if rest_works else '❌ Failed'}")
    print(f"  gRPC API: {'✅ Working' if grpc_works else '❌ Failed'}")
    print("=" * 60)
    
    if rest_works:
        print("\n✅ Recommendation: Use transport='rest' in your code")
    else:
        print("\n❌ Both transports failed. Check your API key and network connection")
