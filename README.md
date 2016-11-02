# crawl_list_300
crawl list 300

## build the docker to crawl
docker-compose build

## crawl all the company pages
docker-compose up

## crawl a specific page
docker-commpose run crawler /opt/crawler/company_page.py {url} {csv_file}
