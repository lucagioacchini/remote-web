# RemoteWeb

This repo hosts a Chrome-based web browser relying on `selenium`.

The browser comes with a local server running on Docker with custom APIs and a python client.

The main elements of the server are:
- A search engine based on DuckDuckGo.
- A web browser based on Chrome.

See the [supported APIs](#supported-apis-and-functionalities) for more details.

## Contents
- [Local Server Installation](#local-server-installation)
- [Client Installation](#client-installation)
- [APIs](#supported-apis-and-functionalities)

## Local Server Installation

Before installing a local server, ensure that Docker is installed in your local machine.
Then, open a terminal and run
```bash
$ ./server_install.sh
```

If the installation succeeds, you should see the `web_scraper` container running on your local machine.

## Client Installation

Install `remoteweb` package through
```bash
$ pip3 install -e .
```
or
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -e .
```

## Supported APIs and Functionalities

- `search`: run a web search. Providing a search query, it returns the top-5 URLs related to the query;
- `scrape`: scrape the content of a web page. Providing the URL of a web page, retrieve the text (not the HTML);
- `download`: locally download a file. Providing the URL of a file, download it locally. **Note** Currently supports only PDF files.