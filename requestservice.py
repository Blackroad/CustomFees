from requests_html import HTMLSession
import re


class HtmlParsHelper(HTMLSession):
    def __init__(self,url):
        super().__init__()
        self.url = url

    def connect_to_url(self):
        try:
            if (HtmlParsHelper.get(self, url=self.url)).status_code == 200:
                return HtmlParsHelper.get(self, url=self.url)
        except Exception as e:
            return(e)

    def get_nbu_rate(self):
        target = self.connect_to_url()
        value = '//div[@class = "idx-rightmenu idx-block-800"]/table[2]//td[2]'
        set = target.html.xpath(value)
        for i in set:
              return float((re.sub('%','', i.text)).replace(',','.'))



a = HtmlParsHelper('https://index.minfin.com.ua/')
print(a.get_nbu_rate())
























