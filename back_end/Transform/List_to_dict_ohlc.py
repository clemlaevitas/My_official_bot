import sys
sys.path.append('.')

from Extract.API_Binance import get_data_from_binance
from Transform.date_conversions import unixtime_to_datetime

def list_to_dict(data, period): 
    result_list = []
    for item in data:
        timestamp = item[0]
        timestamp = unixtime_to_datetime(timestamp, period)
        inner_dict = {
                "Date": timestamp,
                "Open_price": float(item[1]),
                "High_price": float(item[2]),
                "Low_price": float(item[3]),
                "Close_price": float(item[4]),
            }
        result_list.append(inner_dict)
         
    return result_list #list of dictionaries

def prepared_data(coin, start, end, interval): # Should be somewhere else. Not logical to have it here
    last_data = get_data_from_binance(coin, interval, start, end)
    initial_dict = list_to_dict(last_data, interval)

    return initial_dict #this data needs only to be called once