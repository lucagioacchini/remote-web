from flask import Flask, request
from service import Service

app = Flask(__name__)
service = Service()

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    session_id = data.get('session_id')
    if not url:
        return "URL parameter is missing", 400
        
    return service.scrape(url, session_id)


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')
    if not query:
        return "query parameter is missing", 400
    
    return service.search(query)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)