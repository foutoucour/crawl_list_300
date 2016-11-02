import unicodedata
import csv
import os
from contextlib import contextmanager
csv_header = (
    "name",
    "website",
    "rank500",
    "rank300qc",
    "summary",
    "address",
    "number_employee_qc",
    "number_employee_total",
    "income_qc",
    "income_total",
    "profit",
    "assets_qc",
    "assets_total",
    "executives_ceo",
    "executives_vp",
    "services_biz_dev",
    "services_rnd",
    "services_hr",
)

commpany_page_xpaths = {
    'name': '//*[@id="fiche_detail"]/div[2]/div[1]/div[1]/div[1]/h1',
    'rank500': '//*[@id="fiche_detail"]/div[2]/div[1]/div[1]/div[1]/p[1]/strong',
    'rank300qc': '//*[@id="fiche_detail"]/div[2]/div[1]/div[1]/div[1]/p[2]/strong',
    'summary': '//*[@id="fiche_detail"]/div[2]/div[1]/div[2]/div/p',
    'number_employee_qc': '//*[@id="fiche_detail"][2]/div[1]/div[9]/div[1]/table/tbody/tr[1]/td[2]',
    'number_employee_total': '//*[@id="fiche_detail"]/div[2]/div[1]/div[9]/div[1]/table/tbody/tr[2]/td[2]',
    'income_qc': '//*[@id="fiche_detail"]/div[2]/div[1]/div[11]/div[1]/div/table/tbody/tr[1]/td[2]',
    'income_total': '//*[@id="fiche_detail"]/div[2]/div[1]/div[11]/div[1]/div/table/tbody/tr[2]/td[2]',
    'profit': '//*[@id="fiche_detail"]/div[2]/div[1]/div[11]/div[2]/table[1]/tbody/tr/td[2]',
    'assets_qc': '//*[@id="fiche_detail"]/div[2]/div[1]/div[11]/div[2]/table[2]/tbody/tr[1]/td[2]',
    'assets_total': '//*[@id="fiche_detail"]/div[2]/div[1]/div[11]/div[2]/table[2]/tbody/tr[2]/td[2]',
    'executives_ceo': '//*[@id="fiche_detail"]/div[2]/div[1]/div[16]/div[1]/table[1]/tbody/tr[2]/td',
    'executives_vp': '//*[@id="fiche_detail"]/div[2]/div[1]/div[16]/div[1]/table[1]/tbody/tr[2]/td',
    'services_biz_dev': '//*[@id="fiche_detail"]/div[2]/div[1]/div[19]/div[2]/table[1]/tbody/tr[2]/td',
    'services_rnd': '//*[@id="fiche_detail"]/div[2]/div[1]/div[19]/div[2]/table[3]/tbody/tr[2]/td',
    'services_hr': '//*[@id="fiche_detail"]/div[2]/div[1]/div[19]/div[2]/table[5]/tbody/tr[2]/td',
}
commpany_page_website_xpath = '//*[@id="fiche_detail"]/div[2]/div[1]/div[7]/div[2]/table/tbody/tr[5]/td[2]/a'
commpany_page_address_xpath = '//*[@id="fiche_detail"]/div[2]/div[1]/div[7]/div[1]/table/tbody/tr/td/p'

main_page_url = 'http://www.lesaffaires.com/classements/les-300/liste'
main_page_all_a = '//*[@id="classement300"]/div[1]/div/table/tbody/tr/td/a'


def normalize(text):
    return unicodedata.normalize('NFKD', text).encode('utf8', 'ignore')


@contextmanager
def get_csv_writer(csv_file_path):
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, 'wb') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
            writer.writerow(csv_header)
            yield writer
    else:
        with open(csv_file_path, 'a') as csv_file:
            writer = csv.writer(
                csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL
            )

            yield writer
