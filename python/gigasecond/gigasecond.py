import datetime

Giga_SECONDS = 1_000_000_000


def add_gigasecond(moment):
    return moment + datetime.timedelta(seconds=Giga_SECONDS) 
