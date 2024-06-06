from remoteweb.client import WebBrowserClient

# Instantiate the client providing local endpoint
browser = WebBrowserClient(server='localhost', port=5000)

# Run an online search with DuckDuckGo
search_results = browser.search('python programming')

# Print the search results
for idx, result in search_results.items():
    print(f"Url: {result['url']}")
    print(f"Title: {result['title']}")
    print(f"Snippet: {result['snippet']}")
    print()

# Scrape a WebPage
webpage = browser.scrape(search_results['0']['url'])
print(f"Content: {webpage['text']}")