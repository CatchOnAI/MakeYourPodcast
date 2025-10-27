"""
Standalone script to test Jina API connection
This helps debug authentication issues
"""

import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

console = Console()

def test_jina_api():
    """Test Jina API with detailed debugging information"""
    
    # Load environment variables
    load_dotenv()
    
    # Get the API key
    jina_api_key = os.getenv("JINA_API_KEYS", "")
    
    console.print("\n[bold cyan]🔍 Testing Jina API Connection[/bold cyan]\n")
    
    # Debug: Show API key info (masked for security)
    if jina_api_key:
        key_length = len(jina_api_key)
        key_preview = jina_api_key[:10] + "..." + jina_api_key[-10:] if len(jina_api_key) > 20 else jina_api_key
        console.print(f"[green]✓[/green] API Key found")
        console.print(f"  Length: {key_length} characters")
        console.print(f"  Preview: {key_preview}")
        console.print(f"  Has leading whitespace: {jina_api_key != jina_api_key.lstrip()}")
        console.print(f"  Has trailing whitespace: {jina_api_key != jina_api_key.rstrip()}")
        
        # Strip whitespace
        jina_api_key_clean = jina_api_key.strip()
        console.print(f"  After strip: {len(jina_api_key_clean)} characters\n")
    else:
        console.print("[red]✗[/red] JINA_API_KEYS not found in environment!\n")
        return False
    
    # Test URL
    test_url = "https://www.google.com"
    jina_endpoint = f"https://r.jina.ai/{test_url}"
    
    console.print(f"[bold]Test Request:[/bold]")
    console.print(f"  Endpoint: {jina_endpoint}")
    console.print(f"  Method: GET\n")
    
    # Make the request
    headers = {
        "Authorization": f"Bearer {jina_api_key_clean}",
    }
    
    console.print("[bold]Making request...[/bold]\n")
    
    try:
        response = requests.get(
            jina_endpoint,
            headers=headers,
            timeout=30
        )
        
        console.print(f"[bold]Response Status:[/bold] {response.status_code}\n")
        
        if response.status_code == 200:
            content = response.text
            console.print(Panel.fit(
                f"[bold green]✅ Success![/bold green]\n\n"
                f"Response length: {len(content)} characters\n"
                f"First 500 chars:\n\n{content[:500]}...",
                border_style="green",
                title="Jina API Test Result"
            ))
            return True
        else:
            console.print(Panel.fit(
                f"[bold red]❌ Request Failed[/bold red]\n\n"
                f"Status Code: {response.status_code}\n"
                f"Response:\n{response.text}",
                border_style="red",
                title="Error Details"
            ))
            
            # Additional debugging
            console.print("\n[yellow]Debugging Tips:[/yellow]")
            console.print("1. Verify your API key is valid at https://jina.ai/")
            console.print("2. Check if the key has expired")
            console.print("3. Try generating a new API key")
            console.print("4. Make sure there are no extra spaces in your .env file")
            
            return False
            
    except requests.exceptions.Timeout:
        console.print("[red]✗[/red] Request timed out after 30 seconds")
        return False
    except requests.exceptions.RequestException as e:
        console.print(f"[red]✗[/red] Request error: {e}")
        return False
    except Exception as e:
        console.print(f"[red]✗[/red] Unexpected error: {e}")
        import traceback
        console.print(traceback.format_exc())
        return False

def main():
    """Main entry point"""
    success = test_jina_api()
    
    if success:
        console.print("\n[bold green]All tests passed! ✅[/bold green]")
        console.print("Your Jina API configuration is working correctly.\n")
    else:
        console.print("\n[bold red]Tests failed! ❌[/bold red]")
        console.print("Please fix the issues above before running the main script.\n")

if __name__ == "__main__":
    main()

