import datetime


class MyHolydays:
    def __init__(self):
        self.day = datetime.date.day
        self.month = datetime.date.month
        #set of URK_holidays
        self.holy_days = (
            {self.day: 1, self.month: 1}, {self.day: 7, self.month: 1}, {self.day: 8, self.month: 3}, {self.day: 1, self.month: 5}, {self.day: 9, self.month: 5},
            {self.day: 28, self.month: 6}, {self.day: 24, self.month: 8},
            {self.day: 14, self.month: 10}, {self.day: 25, self.month: 12})

    def get_holidays_for_selected_year(self,selected_year_start:int, selected_year_end:int):
        list_of_holidays = []
        #get_list of trinity and easter for period of years
        list_trinity_easter = self.list_of_easter_trinity(selected_year_start,selected_year_end)
        #Generate list of all ukr.holydays
        [list_of_holidays.append((datetime.date(year, i[self.month], i[self.day]))) for i in self.holy_days
         for year in range(selected_year_start, (selected_year_end + 1))]
        #sum the all holidays for period of years + all easters + trinity for period of years
        list_of_holidays = list_of_holidays + list_trinity_easter
        #create one list with holydays + dayoffs
        return sorted(list_of_holidays + self.add_dayoffs(list_of_holidays))

    # Shifting days from Saturday + 2 and Synday + 1 to receive dayoffs
    def add_dayoffs(self, holiday_list):
        list_of_dayoffs = []
        for i in holiday_list:
            if i.weekday() == 5:
                weekand = i + datetime.timedelta(2)
                list_of_dayoffs.append(weekand)
            elif i.weekday() == 6:
                weekand = i + datetime.timedelta(1)
                list_of_dayoffs.append(weekand)
        return list_of_dayoffs

    def get_easter_days(self,selected_year:int):
        M = 15
        N = 6
        a = selected_year % 19
        b = selected_year % 4
        c = selected_year % 7
        d = (19*a + M)%30
        e = (2*b + 4*c + 6*d + N) % 7
        z = d + e
        easter_month = (z + 25) // 35 + 3
        easter_day = z + 22 - 31 * (easter_month // 4)
        #will work only to 2100 year, if later , timedelta == 14
        easter = (datetime.date(selected_year, easter_month, easter_day) + datetime.timedelta(13))
        return (easter)


    def get_trinity(self, easter):
        trinity = easter + datetime.timedelta(50)
        return (trinity)

    def list_of_easter_trinity(self,year_from, year_to):
        list = []
        [(list.append(self.get_easter_days(i)+datetime.timedelta(13)),
          list.append(self.get_easter_days(i)))for i in range(year_from, year_to + 1, 1)]
        return list
















