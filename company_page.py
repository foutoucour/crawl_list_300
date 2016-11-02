#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import logging
import click
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import config

logger = logging.getLogger(__name__)
logging.basicConfig()


def save_company_details(url, csv_file_path):
    """Crawl the given url and save it to the give csv file.

    :param str url: url of the page to crawl.
    :param str csv_file_path: path to the page to save to.
    :return: Mapping of the details extracted from the page.
    :rtype: dict
    """
    print('crawling {}'.format(url))
    details = {}
    driver = webdriver.PhantomJS()
    driver.get(url)

    for label, xpath in config.commpany_page_xpaths.iteritems():
        try:
            element = driver.find_element_by_xpath(xpath)
            text = element.text
        except NoSuchElementException:
            text = 'nd'

        if isinstance(text, unicode):
            text = config.normalize(text)
        details[label] = text

    # website
    # special case as we want the href instead of the text as the text can be trunked.
    try:
        website_element = driver.find_element_by_xpath(
            config.commpany_page_website_xpath)
        text = website_element.get_attribute('href')
    except NoSuchElementException:
        text = 'nd'
    details['website'] = text

    address = ''
    try:
        for element in driver.find_elements_by_xpath(config.commpany_page_address_xpath):
            address += config.normalize(element.text)
            address += ' '
    except NoSuchElementException:
        address = 'nd'
    details['address'] = address.strip()

    values = []
    for row in config.csv_header:
        values.append(details[row])

    with config.get_csv_writer(csv_file_path) as writer:
        writer.writerow(values)

    driver.close()
    print('done {}'.format(url))
    return values


@click.command()
@click.argument('url')
@click.argument('csv_file_path')
def command(url, csv_file_path):
    """Command line to crawl the page."""
    return save_company_details(url, csv_file_path)


if __name__ == '__main__':
    command()
