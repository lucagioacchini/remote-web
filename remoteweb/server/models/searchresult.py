class SearchResult():
    def __init__(self, query, entries):
        self.query = query
        self.entries = entries
    
    def to_dict(self):
        obj = {}
        for cnt, item in enumerate(self.entries):
            obj[cnt] = {
                'title':item['title'],
                'url':item['href'],
                'snippet':item['body']
            }
        return obj
