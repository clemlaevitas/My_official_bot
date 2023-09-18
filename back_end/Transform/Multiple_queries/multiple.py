import requests
#look at notes, functions calling each other. Last function will be called in main

#IMPOrTANT THIS NEEDS TO WOrK for OHLC but also EMA and KC !!!


#TO PUT IN MAIN
# if data_points > 500:
#     print("Data exceeds 500 points. Splitting into multiple requests.")
# else:
#     pass

# #1) Create couples
def create_couples(start_date, end_date, period):
    delta = end_date - start_date # look at what type of date used..

    if period == '1d':
        data_points = delta.days + 1  
    elif period == '1h':
        data_points = (delta.days * 24) + 1  
    elif period == '1m':
        data_points = (delta.days * 24 * 60) + 1 
    
    # Calc number of queries needed
    num_queries = data_points // 500 + 1

    date_ranges = []
    for i in range(num_queries):
        query_start_date = start_date + datetime.timedelta(days=i * 500)
        query_end_date = min(start_date + datetime.timedelta(days=(i + 1) * 500 - 1), end_date) #verify the -1 to you ensure that query_end_date remains within the specified date range and doesn't exceed it
        date_ranges.append((query_start_date, query_end_date))

    return date_ranges

#2) Create ULrS

def create_urls(couples, start_date, end_date, frequency_ST, frequency_LT, period):
    urls = []
    for couple in couples:
        #should be couple 0 and 1 here
        urls.append(f'http://127.0.0.1:5000/EMA?start_date={unix_query_start_date}&end_date={unix_query_end_date}&smoothing_factor={smoothing_factor}&period={period}&frequLT={frequency_LT}&frequST={frequency_ST}')
        #ça renvoie donc au main!!!
        return urls

    #question: make a list of urls? To call it together?!!

#3) fetch data and then append the data together 

def fetch_and_append_requests(start_date, end_date, frequency_ST, frequency_LT, period):

    data = []
    for url in urls:
        result = requests.get(url)
        req_result = HTML_req.json()
        data.append(req_result)

# Function to transform to unix time and then retransform again (already exist maybe code)

# I SHOULD create these two function in general to call them when needed!!!

    # for i, (query_start_date, query_end_date) in enumerate(date_ranges):
    #     unix_query_start_date = int(datetime.datetime(
    #         query_start_date.year, query_start_date.month, query_start_date.day).timestamp()) * 1000
    #     unix_query_end_date = int(datetime.datetime(
    #         query_end_date.year, query_end_date.month, query_end_date.day).timestamp()) * 1000
        





