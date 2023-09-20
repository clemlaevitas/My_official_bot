# import datetime: datetime is a module and datetime is a class as well
#there are many classes strtime, date, timedelta, timstamp,..
#best practice is to do from datetime import datetime

from datetime import datetime
# import datetime

def datetime_to_unixtime(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime.datetime object")
    unix = int(dt.timestamp())
    return unix 
    #here not *1000 because not done, to verify later

def unixtime_to_datetime(item, period):
    if period == "1d":
        return datetime.utcfromtimestamp(item/1000).strftime('%Y-%m-%d')
    elif period == "1h":
        return datetime.utcfromtimestamp(item/1000).strftime('%Y-%m-%d-%H:%M:%S')
    #not for 1m for the moment


#example
# dt = datetime(2023, 9, 18)
# unix = datetime_to_unixtime(dt)
# print(unix)

# unix_time = 1692499200
# unix_time = unix_time * 1000  # This represents 2023-09-18 00:00:00 UTC
# date_time = unixtime_to_datetime(unix_time, '1d')
# print(date_time)
