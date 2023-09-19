import requests
import datetime
from Transform.list_to_dict_ohlc import prepared_data

# import datetime

# 0) Number of data points
def number_data_points(start_unix, end_unix, period):

    # start_unix = int(start_unix/1000) no needed anymore because dateconversion function without correction
    # end_unix = int(end_unix/1000)

    delta = end_unix - start_unix

    if period == '1d':
        data_points = delta // (24 * 3600) + 1
    elif period == '1h':
        data_points = delta // 3600 + 1
    elif period == '1m':
        data_points = delta // 60 + 1

    return data_points

# 1) Create couples
def create_couples(start_unix, end_unix, datapoints):

    # start_unix = int(start_unix/1000)
    # end_unix = int(end_unix/1000)

    num_queries = datapoints // 500 + 1
    print('this is num_queries', num_queries)

    date_ranges = []
    for i in range(num_queries):
        query_start_unix = start_unix + i * 500 * 24 * 3600  # Convert days to seconds
        query_end_unix = min(start_unix + (i + 1) * 500 * 24 * 3600 - 1, end_unix)
        date_ranges.append((query_start_unix, query_end_unix))

    return date_ranges

# 2) Fetch data
def fetch_data(couples, period, partial = False):
    data = []
    for elem in couples:
        start_unix = elem[0]
        end_unix = elem[1]
        start_unix = start_unix * 1000 #ONLY HErE in entire code !!!
        end_unix = end_unix * 1000
        results = prepared_data("BTCUSDT", start_unix, end_unix, period, partial)
        data.extend(results)
    return data

#example

start_date = 1689698552
end_date = 1695055353
period = "1d"

datapoints = number_data_points(start_date, end_date, period)
couples = create_couples(start_date, end_date, datapoints)
data = fetch_data(couples, period)

print(data)
