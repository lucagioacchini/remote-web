FROM python:3.9

USER root

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable unzip && \
    rm -rf /var/lib/apt/lists/*

    
# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install requirements
RUN pip install selenium \
                flask \
                html2text \
                duckduckgo_search

# Keep the container running (you can replace this with your actual application command)
COPY . /home/remoteweb_server
ENTRYPOINT [ "python3", "/home/remoteweb_server/server_start.py" ]