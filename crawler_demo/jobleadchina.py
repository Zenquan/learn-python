import requests
import pandas as pd
# from lxml import etree

class JobLeadChina:
    def __init__(self, max_age):
        self.start_urls = [
            'http://www.jobleadchina.com/job?job_industry=Teaching'
            '&company_name=&page={}'.format(page) for page in range(1, max_age+1)
        ]

    def get_data(self):
        for url in self.start_urls:
            res = requests.get(url)
            page = url.split('=')[-1]
            print(res.text, page)

    # @staticmethod
    # def parse_data(res, page):
    #     if res.status_code == '200':
    #         parsed = etree.HTML(res.text)
    #
    #         if page=='1':
    #             data.to_csv
    #
    #     else:
    #         print('第{}页未连接成功'.format(page))

if __name__=='__main__':
    job = JobLeadChina(96)
    job.get_data()