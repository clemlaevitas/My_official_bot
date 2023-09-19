import datetime
from Transform.date_conversions import datetime_to_unixtime #here error to call the function...
from Transform.multiple_queries import number_data_points, create_couples, fetch_data

def OHLC_route(start_date, end_date, period, partial = False):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    start_date = datetime_to_unixtime(start_date) #NOT *1000!!
    end_date = datetime_to_unixtime(end_date)
    datapoints = number_data_points(start_date, end_date, period)
    couples = create_couples(start_date, end_date, datapoints)
    data = fetch_data(couples, period, partial)
    
    return data #for the moment list of dictionaries
