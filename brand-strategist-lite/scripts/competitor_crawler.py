import sys
import json
import os
import re
from playwright.sync_api import sync_playwright

def clean_text(text):
    """
    Cleans up the text by removing excessive whitespace.
    """
    if not text:
        return ""
    # Replace multiple newlines/spaces with a single one, but keep paragraph breaks
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def crawl_site(url):
    """
    Crawls a dynamic website using Playwright.
    """
    content = {
        "url": url,
        "title": "",
        "text": "",
        "error": None
    }

    try:
        with sync_playwright() as p:
            # Launch browser (headless by default)
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                viewport={'width': 1920, 'height': 1080}
            )
            page = context.new_page()
            
            # Go to URL with timeout
            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
            except Exception as e:
                # If networkidle times out, try domcontentloaded as fallback
                print(f"Warning: Network idle timeout for {url}, trying domcontentloaded...")
                page.goto(url, wait_until="domcontentloaded", timeout=15000)

            # Get Title
            content["title"] = page.title()

            # Smart Content Extraction
            # 1. Try to find the main content article
            main_element = page.locator('main, article, #content, .content, #main').first
            
            if main_element.count() > 0:
                # If main content exists, focus on that
                text_content = main_element.inner_text()
            else:
                # Fallback to body but try to remove header/footer/nav via JS evaluation if possible
                # or just get the whole body text
                text_content = page.locator('body').inner_text()

            # Basic cleaning of the text
            content["text"] = clean_text(text_content)[:8000] # Increased limit slightly for better context
            
            browser.close()

    except Exception as e:
        content["error"] = str(e)
        print(f"Error crawling {url}: {e}")

    return content

def main():
    # Detect Project Root (needed strictly for imports here)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    
    # Add script dir to sys.path to allow importing state_manager
    sys.path.append(script_dir)
    try:
        from state_manager import StateManager
    except ImportError:
        print("Error: Could not import state_manager.py")
        sys.exit(1)

    manager = StateManager(project_root)
    results = []

    # Mode 1: URL from Arguments
    if len(sys.argv) > 1:
        input_val = sys.argv[1]
        if input_val.startswith('http'):
            print(f"Crawling single URL: {input_val}")
            res = crawl_site(input_val)
            results.append(res)
            # Also add to state if valid
            if not res.get("error"):
                manager.add_competitor_url(input_val)
        elif input_val == "state":
             print("Reading URLs from project_state.json...")
             urls = manager.get_competitor_urls()
             if not urls:
                 print("No competitor URLs found in state.")
             for url in urls:
                 results.append(crawl_site(url))
        elif os.path.exists(input_val):
             # Legacy config file support
             print(f"Reading from config file: {input_val}")
             with open(input_val, 'r', encoding='utf-8') as f:
                config = json.load(f)
                urls = config.get("competitor_urls", [])
                for url in urls:
                    results.append(crawl_site(url))
                    manager.add_competitor_url(url) # Sync to state
    
    # Mode 2: Default (Read from State)
    else:
        print("No arguments provided. Reading URLs from project_state.json...")
        urls = manager.get_competitor_urls()
        if not urls:
             # Fallback to targets.json if state is empty
             targets_path = os.path.join(project_root, "config", "targets.json")
             if os.path.exists(targets_path):
                 print("State empty. Falling back to config/targets.json")
                 with open(targets_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    urls = config.get("competitor_urls", [])
                    for url in urls:
                        manager.add_competitor_url(url)
                        results.append(crawl_site(url))
             else:
                 print("No URLs found to crawl.")
                 return

    # Output directory handling
    # (project_root is already defined at start of main)
    if not os.path.exists(os.path.join(project_root, "stage_2_market_analysis")):
         project_root = os.getcwd() # Fallback

    output_dir = os.path.join(project_root, "stage_2_market_analysis", "competitors")
    os.makedirs(output_dir, exist_ok=True)
    
    for i, res in enumerate(results):
        # Create a safe filename from domain if possible, else index
        try:
            domain = res['url'].split('//')[1].split('/')[0].replace('.', '_')
            filename = f"{domain}_{i}.json"
        except:
            filename = f"crawled_site_{i}.json"
            
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        
        # Update State
        manager.update_crawled_data(filepath)
    
    print(f"Successfully crawled {len(results)} sites and saved to {output_dir}")
    print("Project state updated.")
if __name__ == "__main__":
    main()
