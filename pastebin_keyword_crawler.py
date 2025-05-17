import requests
from bs4 import BeautifulSoup

# Pastebin archive URL
PASTEBIN_ARCHIVE = "https://pastebin.com/archive"
KEYWORDS = ["crypto", "bitcoin", "ethereum", "wallet", "telegram"]

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_recent_pastes():
    try:
        res = requests.get(PASTEBIN_ARCHIVE, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.select("table.maintable a")
        paste_links = ["https://pastebin.com" + link['href'] for link in links if link['href'].startswith('/')]
        return paste_links[:10]  # limit for demo
    except Exception as e:
        print("Error fetching archive:", e)
        return []

def scan_paste(link):
    try:
        res = requests.get(link, headers=headers)
        content = res.text.lower()
        for keyword in KEYWORDS:
            if keyword in content:
                snippet = content[:300].replace('\n', ' ')
                print(f"[+] Found keyword '{keyword}' in {link}")
                return f"[{keyword.upper()}] {link}\nSnippet: {snippet}\n\n"
    except Exception as e:
        print("Error scanning paste:", e)
    return ""

def main():
    print("🔍 Crawling Pastebin for keywords...")
    links = get_recent_pastes()
    print(f"Found {len(links)} pastes.")
    
    results = []
    for link in links:
        result = scan_paste(link)
        if result:
            results.append(result)

    if results:
        with open("found_keywords.txt", "w", encoding="utf-8") as f:
            f.writelines(results)
        print("✅ Results saved to found_keywords.txt")
    else:
        print("❌ No keywords found in recent pastes.")

if __name__ == "__main__":
    main()
