docker build -t web_scraper_api remoteweb/server/.
docker run -d --name web_scraper -p 5000:5000 web_scraper_api