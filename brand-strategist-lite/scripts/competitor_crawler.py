import sys
import json
import os
import requests
from bs4 import BeautifulSoup

def crawl_site(url):
    """
    簡單的爬蟲函數，抓取目標網站的核心文字內容。
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 移除指令碼與樣式
        for script in soup(["script", "style"]):
            script.decompose()

        # 抓取關鍵區塊文字
        content = {
            "url": url,
            "title": soup.title.string if soup.title else "",
            "text": soup.get_text(separator='\n', strip=True)[:5000] # 限制長度以節省 token
        }
        return content
    except Exception as e:
        return {"url": url, "error": str(e)}

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 competitor_crawler.py <config_path_or_url>")
        sys.exit(1)

    input_val = sys.argv[1]
    results = []

    if input_val.startswith('http'):
        # 直接爬取單個 URL
        results.append(crawl_site(input_val))
    else:
        # 從設定檔讀取多個 URL
        if os.path.exists(input_val):
            with open(input_val, 'r') as f:
                config = json.load(f)
                urls = config.get("competitor_urls", [])
                for url in urls:
                    results.append(crawl_site(url))
        else:
            print(f"Error: File {input_val} not found.")
            sys.exit(1)

    # 將結果存入 stage_2 資料夾
    # Update to current project structure: script is in brand-strategist-lite/scripts/
    # Output should go to stage_2_market_analysis/competitors/ which is in the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))
    output_dir = os.path.join(project_root, "stage_2_market_analysis", "competitors")
    os.makedirs(output_dir, exist_ok=True)
    
    for i, res in enumerate(results):
        filename = f"crawled_site_{i}.json"
        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully crawled {len(results)} sites and saved to {output_dir}")

if __name__ == "__main__":
    main()
