import sys
sys.path.append('.')

from datetime import datetime
from Transform.date_conversions import datetime_to_unixtime
from Transform.multiple_queries import number_data_points, create_couples, fetch_data
from Extract.new_start_date import match_EMAs_length

def dates_modif(start_date, end_date, period, frequ_LT):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    start_date_unix = datetime_to_unixtime(start_date) #NOT *1000!!
    end_date_unix = datetime_to_unixtime(end_date)

    start_date_unix_updated = match_EMAs_length(start_date_unix, frequ_LT, period)
    
    return start_date_unix_updated, end_date_unix

def OHLC_route(start_date, end_date, period, frequ_LT = 0):
    start_date, end_date = dates_modif(start_date, end_date, period, frequ_LT)

    datapoints = number_data_points(start_date, end_date, period)
    couples = create_couples(start_date, end_date, datapoints)
    data = fetch_data(couples, period)
    
    return data #for the moment list of dictionaries

#example
# start_date = '2021-08-01'
# end_date = '2023-09-20'
# start_date = datetime.strptime(start_date, '%Y-%m-%d')
# end_date = datetime.strptime(end_date, '%Y-%m-%d')
# print(start_date, end_date)
# start_date= datetime(2021, 8, 1)
# end_date= datetime(2023, 9, 20)
# period='1d'
# frequ_LT=10

# start_date, end_date = dates_modif(start_date, end_date, period, frequ_LT)
# print(start_date, end_date)

# data=OHLC_route(start_date, end_date, period, frequ_LT)
# print(data)