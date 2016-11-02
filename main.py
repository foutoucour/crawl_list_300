#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import time
import logging
from selenium import webdriver

import config
import company_page

logger = logging.getLogger(__name__)
logging.basicConfig()


def main_page(url):
    """Crawl the main page to find all the url from the list.

    :param str url: url of the main page.
    :return: urls found in the list
    :rtype: list
    """
    driver = webdriver.PhantomJS()
    print('crawling {}'.format(url))
    driver.get(url)
    elements = driver.find_elements_by_xpath(config.main_page_all_a)
    urls = [element.get_attribute('href') for element in elements]
    driver.close()
    print('done {}'.format(url))
    return urls


def main(csv_file_path=None):
    """Crawl the list of the main page to save details of the companies.

    :param str csv_file_path: path to the page to save to. Default list_300.csv
    """
    if not csv_file_path:
        csv_file_path = os.path.join(os.path.dirname(__file__), 'list_300.csv')
    urls = main_page(config.main_page_url)

    for i, url in enumerate(urls):
        print('url #{}'.format(i))
        company_page.save_company_details(url, csv_file_path)
        time.sleep(1)


if __name__ == '__main__':
    main()
