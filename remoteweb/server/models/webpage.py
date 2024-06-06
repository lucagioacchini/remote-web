from html2text import HTML2Text

class WebPage():
    def __init__(self, url, html):
        self.url = url
        self.html = html
        self.text = self._extract_text()

    def _extract_text(self):
        html_converter = HTML2Text()
        html_converter.wrap_links = True
        html_converter.wrap_lists = True
        extracted_text = html_converter.handle(self.html)
        return extracted_text
    
    def to_dict(self):
        obj = {
            'url':self.url,
            'html':self.html,
            'text':self.text
        }
        return obj