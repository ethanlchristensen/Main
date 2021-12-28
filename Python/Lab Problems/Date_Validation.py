def checkone():
    calendar = {
        'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31
    }
    month = input('Enter 3 character abbreviation for month: ')
    day = int(input('Enter day: '))
    year = int(input('Enter year: '))
    if month in calendar:
        if month == 'Feb':
            days = calendar.get(month)
            if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
                if day > 0 and day <= days + 1:
                    print('{:s} {:d}, {:d} is a valid date.'.format(month, day, year))
                else:
                    print('{:s} {:d}, {:d} isn\'t a valid date.'.format(month, day, year))    
            else:
                if day > 0 and day <= days:
                    print('{:s} {:d}, {:d} is a valid date.'.format(month, day, year))
                else:
                    print('{:s} {:d}, {:d} isn\'t a valid date.'.format(month, day, year))
        else:
            days = calendar.get(month)
            if day > 0 and day <= days:
                print('{:s} {:d}, {:d} is a valid date.'.format(month, day, year))
            else:
                print('{:s} {:d}, {:d} isn\'t a valid date.'.format(month, day, year))
    else:
        print('{:s} {:d}, {:d} isn\'t a valid date.'.format(month, day, year))
        
def checktwo():
    calendar = {
        'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31
    }

    def leap_check(year):
        if (year%4==0 and year%100 != 0) or year%400==0:
            return True

    flag = 0
    month = input('Enter 3 character abbreviation for month: ')
    day = int(input('Enter day: '))
    year = int(input('Enter year: '))
    if isinstance(day, int) and isinstance(year, int):
        if month in calendar:
            if year >= 1752:
                if month == 'Feb' and leap_check(year):
                    if day > 0 and day <= calendar.get(month) + 1:
                        flag += 1
                    else:
                        if day > 0 and day <= calendar.get(month):
                            flag += 1
    if flag == 0:
        print("{} {}, {} isn't a valid date.".format(month, day, year))
    else:
        print('{} {}, {} is a valid date.'.format(month, day, year))


checkone()
checktwo()