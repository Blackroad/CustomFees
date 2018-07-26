from requests_html import HTMLSession
import re
from datetime import datetime
import workdays
from holydays import MyHolydays
import pandas

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
                value = '//div[@id="idx-wrapper"]//tr//td[2][@align="right"]'
                set = target.html.xpath(value)
                set.reverse()
                return float((re.sub('%', '', set[0].text)).replace(',', '.'))
        except Exception as e:
            print('URL is incorrect or connection failed \n\bReason:', e)


    def get_nbu_rate_for_all_periods(self):
            if (HtmlParsHelper.get(self, url=self.url)).status_code == 200:
                 target = HtmlParsHelper.get(self, url=self.url)
                 set = target.html.xpath('//div[@id="idx-wrapper"]//tr//td[@align="left"]')
                 value = target.html.xpath('//div[@id="idx-wrapper"]//tr//td//big')
                 new = []
                 for i,j in zip(set,value):
                     list = re.findall(r'\d{2}\.\d{2}\.\d{4}',i.text)
                     list2 = [float(re.sub(',','.', j.text))]
                     set_of_dates = ([datetime.date(datetime.strptime(elem,'%d.%m.%Y')) for elem in list])
                     new.append(set_of_dates + list2)
                 return new

    def get_dates(self,date_start,date_end,dept_value):
        all_rates = self.get_nbu_rate_for_all_periods()
        pd = pandas.date_range(datetime.date(date_start),datetime.date(date_end))
        holidays = MyHolydays()
        sum = 0
        dept = 0
        for item in all_rates:
            #if rates are in range of defined dates
            if (item[0] and item[1]) in pd:
                urk_holidays = holidays.get_holidays_for_selected_year(item[0].year, item[1].year)
                clear_days = abs(workdays.networkdays(item[1], item[0], urk_holidays))
                dept = dept_value * 2 * item[2] / 100 / 365 * clear_days
            elif len(item) < 2:
                urk_holidays = holidays.get_holidays_for_selected_year(item[0].year, item[0].year)
                clear_days = abs(workdays.networkdays(item[1], item[0], urk_holidays))
                dept = dept_value * 2 * item[1] / 100 / 365 * clear_days
            sum +=dept
        return sum





























