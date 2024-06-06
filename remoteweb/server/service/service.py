from selenium import webdriver
from models import SearchResult, WebPage
from duckduckgo_search import DDGS

class Service:
    def __init__(self):
        self.sessions = {}
        
    def get_session(self, session_name):
        if session_name not in self.sessions:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            self.sessions[session_name] = webdriver.Chrome(options=options)
        return self.sessions[session_name]

    def scrape(self, url, session_name='default'):
        driver = self.get_session(session_name)
        driver.get(url)
        html_text = driver.page_source
        webpage = WebPage(url=url, html=html_text)
        return webpage.to_dict()

    def search(self, query):
        results = DDGS().text(query, max_results=5)
        search_result = SearchResult(query, results)
        return search_result.to_dict()