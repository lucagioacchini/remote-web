from pypdf import PdfReader
import requests
import random
import json

class WebBrowserClient():
    def __init__(self, server='localhost', port=5000):
        self.session_id = self._generate_session_id()
        self.endpoint = f'http://{server}:{port}'

    def _generate_session_id(self):
        return ''.join(random.choice('0123456789ABCDEF') for i in range(16))
    
    def run(self, url, data):
        headers = headers = {
            'Content-Type': 'application/json'
        }
        url = f'{self.endpoint}/{url}'
        response = requests.post(
            url=url, 
            data=json.dumps(data), 
            headers=headers
        )
        print(response.text)
        return eval(response.text)

    def scrape(self, url):
        data = {
            "url":url,
            "session_id": self.session_id
        }

        return self.run(url='scrape', data=data)
    
    def search(self, query):
        data = {
            "query":query,
            "session_id": self.session_id
        }

        return self.run(url='search', data=data)

    def download(self, file_url):
        # Send a GET request to the URL
        response = requests.get(file_url, stream=True)
        fname = file_url.split('/')[-1]

        # Open a local file with write-binary mode
        if '.pdf' not in fname: fname = f'{fname}.pdf'
        with open(f'/tmp/{fname}', 'wb') as file:
            # Iterate over the response data in chunks
            for chunk in response.iter_content(chunk_size=8192):
                # Write each chunk to the local file
                file.write(chunk)

        # Check if the file is actually a PDF
        try: 
            PdfReader(f'/tmp/{fname}').pages[0].extract_text()

            return f'Successfully downloaded file {fname}'
        except: 
            return f'The provided link is not referred to a .pdf file.'