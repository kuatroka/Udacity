# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


""" This is a helper procedure that determines if the first day is earlier than the second day"""


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year2 > year1:
        return True
    if year2 == year1:
        if month2 > month1:
            return True
        if month2 == month1:
            return day2 > day1
    return False

print dateIsBefore(2012, 1, 11, 2012, 1, 1)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    if month2 >= month1:
        if day2 >= day1:
            dif_days = ((year2 - year1) * 360) + ((month2 - month1) * 30) + day2 - day1
            return dif_days
        else:
            dif_days = ((year2 - year1) * 360) + ((month2 - month1) * 30) + (day2 + 30 - day1)
            return dif_days
    else:
        if day2 >= day1:
            dif_days = ((year2 - year1) * 360) + ((month2 + 12 - month1) * 30) + day2 - day1
            return dif_days
        else:
            dif_days = ((year2 - year1) * 360) + ((month2 + 12 - month1) * 30) + (day2 + 30 - day1)
            return dif_days


def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()


