import datetime


class MyHolydays:
    def __init__(self):
        self.day = datetime.date.day
        self.month = datetime.date.month
        self.holy_days = (
            {self.day: 1, self.month: 1}, {self.day: 7, self.month: 1}, {self.day: 8, self.month: 3}, {self.day: 1, self.month: 5}, {self.day: 9, self.month: 5},
            {self.day: 28, self.month: 6}, {self.day: 24, self.month: 8},
            {self.day: 14, self.month: 10}, {self.day: 25, self.month: 12})

    def get_holidays_for_selected_year(self,selected_year_start:int, selected_year_end:int):
        list_of_holidays = []
        list_of_dayoffs = []
        for year in range(selected_year_start,(selected_year_end+1)):
            [list_of_holidays.append(datetime.date(year, i[self.month], i[self.day])) for i in self.holy_days]
        for i in list_of_holidays:
            if i.weekday() == 5:
                weekand = i + datetime.timedelta(2)
                list_of_dayoffs.append(weekand)
            elif i.weekday() == 6:
                weekand = i + datetime.timedelta(1)
                list_of_dayoffs.append(weekand)
        list_of_holidays = list_of_holidays + list_of_dayoffs
        return (list_of_holidays)

