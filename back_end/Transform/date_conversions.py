# import datetime: datetime is a module and datetime is a class as well
#there are many classes strtime, date, timedelta, timstamp,..
#best practice is to do from datetime import datetime

from datetime import datetime

def datetime_to_unixtime(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime.datetime object")
    unix = int(dt.timestamp())
    return unix 

def unixtime_to_datetime(unix_time):
    unix_time = int(unix_time)
    return datetime.utcfromtimestamp(unix_time)


#example
dt = datetime(2023, 9, 18)
unix = datetime_to_unixtime(dt)
print(unix)

unix_time = 1692499200
unix_time = unix_time * 1000  # This represents 2023-09-18 00:00:00 UTC
date_time = unixtime_to_datetime(unix_time)
print(date_time)

#I think need to do times or divided by 1000 for BINANCE API