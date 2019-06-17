import datetime
from calendar import day_name


class MeetupDayException(Exception):
    pass


def weekdays_in_month(year, month, weekday):
    """Return all 4/5 dates with given weekday."""
    date = datetime.date(year, month, 1)
    date += datetime.timedelta(days=(weekday - date.weekday()) % 7)
    first_to_fifth = (
        date + datetime.timedelta(weeks=i)
        for i in range(6)
    )
    return [
        date
        for date in first_to_fifth
        if date.month == month
    ]

    
def meetup_day(year, month, weekday, nth):
    day_names = list(day_name)
    shift_by = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last': -1}
    dates = weekdays_in_month(year, month, day_names.index(weekday))
    if nth == 'teenth':
        return next(date for date in dates if date.day > 12)
    try:
        date = dates[shift_by[nth]]
    except IndexError:
        raise MeetupDayException('Date does not exist.') from None
    return date
