def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    print(year, month, day)
    nextD = day
    nextM = month
    nextY = year
    if day != 30:
        nextD += 1
    else:
        nextD = 1

    if month != 12 and day != 30:
        nextM = month
    elif month == 12 and day != 30:
        nextM = month
    elif month != 12 and day == 30:
        nextM += 1
    else:
        nextM = 1

    if month == 12 and day == 30:
        nextY += 1

    return nextY, nextM, nextD

print nextDay(3000, 11, 3)
