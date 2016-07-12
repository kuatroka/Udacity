def nextDay(year, month, day):
    """Warning this version incorrectly assumes that all the months have 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


print nextDay(2000, 11, 31)
