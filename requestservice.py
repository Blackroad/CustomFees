from requests_html import HTMLSession
import re
from datetime import datetime


class HtmlParsHelper(HTMLSession):
    def __init__(self):
        super().__init__()
        self.url = 'https://index.minfin.com.ua/banks/nbu/refinance/'

    def connect_to_url(self):
        try:
            if (HtmlParsHelper.get(self, url=self.url)).status_code == 200:
                return HtmlParsHelper.get(self, url = self.url)
        except Exception as e:
            return(e)

    def get_nbu_rate(self):
        try:
            if (HtmlParsHelper.get(self, url=self.url)).status_code == 200:
                target = HtmlParsHelper.get(self, url=self.url)
                value = '//div[@class = "idx-rightmenu idx-block-800"]/table[2]//td[2]'
                set = target.html.xpath(value)
                for i in set:
                    return float((re.sub('%', '', i.text)).replace(',', '.'))
        except Exception as e:
            print('URL is incorrect or connection failed \n\bReason:', e)


    def get_nbu_rate_for_all_periods(self):
            if (HtmlParsHelper.get(self, url=self.url)).status_code == 200:
                 target = HtmlParsHelper.get(self, url=self.url)
                 set = target.html.xpath('//div[@id="idx-wrapper"]//tr//td[@align="left"]')
                 value = target.html.xpath('//div[@id="idx-wrapper"]//tr//td//big')
                 list =[]
                 for i,j in zip(set,value):
                     value = (re.findall(r'\d{2}\.\d{2}\.\d{4}',i.text))
                     value.append(j.text)
                     print (value)




                 # dates = [datetime.date(datetime.strptime((re.findall(r'\d{2}\.\d{2}\.\d{4}',i.text)[0]),'%d.%m.%Y')) for i in set]










test = HtmlParsHelper()
print(test.get_nbu_rate_for_all_periods())


























