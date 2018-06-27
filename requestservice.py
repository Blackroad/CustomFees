from requests_html import HTMLSession
import re


class HtmlParsHelper(HTMLSession):
    def __init__(self):
        super().__init__()
        self.url = 'https://index.minfin.com.ua/'

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





























