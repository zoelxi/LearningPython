class Date:
    '''class to represent a date'''

    def __init__(self,month,day,year):
        '''Date(month,day,year) -> Date'''
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        '''str(Date) -> str
        returns date in readable format'''
        # list of strings for the months
        months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul',
                  'Aug','Sep','Oct','Nov','Dec']
        output = months[self.month] + ' ' # month
        output += str(self.day) + ', '  # day
        output += str(self.year)
        return output

    def go_to_next_day(self):
        '''Date.go_to_next_day()
        advances the date to the next day'''
        # list with the days in the month
        daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        # check for leap year
        isLeapYear = self.year%4 == 0 and \
                     (self.year%100 != 0 or self.year%400 == 0)
        if self.month == 2 and isLeapYear:
            if self.day == 29:
                self.day = 1
                self.month += 1
            elif self.day == 28:
                self.day += 1
        elif self.day == 31 and self.month == 12:
            self.day = 1
            self.month = 1
            self.year += 1
        elif daysInMonth[self.month] == self.day:
            self.day = 1
            self.month += 1
        else:
            self.day += 1

d = Date(10,19,2004)
d.go_to_next_day()
print(d)
        
            
