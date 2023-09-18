from Extract.API_Binance import get_data_from_binance
from datetime import datetime

def timestamp_to_date(item, period): #maybe put elsewere as need for EMA, KC ect to form list of dict!!!!
    if period == "1d":
        return datetime.utcfromtimestamp(item/1000).strftime('%Y-%m-%d')
    elif period == "1h":
        return datetime.utcfromtimestamp(item/1000).strftime('%Y-%m-%d-%H:%M:%S')
    #not for 1m for the moment

def list_to_dict(data, period): 
    result_list = []
    for item in data:
        timestamp = item[0]
        timestamp = timestamp_to_date(timestamp, period)
        inner_dict = {
                "Date": timestamp,
                "Open_price": float(item[1]),
                "High_price": float(item[2]),
                "Low_price": float(item[3]),
                "Close_price": float(item[4]),
            }
        result_list.append(inner_dict)
    return result_list #list of dictionaries

#need to think here - should I do this in the MAIN? or here?
def prepared_data(coin, start, end, interval):
    last_data = get_data_from_binance(coin, interval, start, end)
    initial_dict = list_to_dict(last_data, interval)

    return initial_dict #this data needs only to be called once