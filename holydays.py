import datetime
import workdays




class MyHolydays:
    def __init__(self):
        self.day = datetime.date.day
        self.month = datetime.date.month
        self.holy_days = (
            {self.day: 1, self.month: 1}, {self.day: 7, self.month: 1}, {self.day: 8, self.month: 3}, {self.day: 1, self.month: 5}, {self.day: 9, self.month: 5},
            {self.day: 28, self.month: 6}, {self.day: 24, self.month: 8},
            {self.day: 14, self.month: 10}, {self.day: 25, self.month: 12})

    def get_holidays_for_selected_year(self,selected_year:int):
        list = []
        list_of_holidays = (datetime.date(selected_year,i[self.month],i[self.day]) for i in self.holy_days)















myclass = MyHolydays()
myclass.get_holidays_for_selected_year(2017)



