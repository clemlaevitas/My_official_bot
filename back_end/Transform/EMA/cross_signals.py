def crossing(data): #is a list of dictionary with EMA_ST and EM_LT
    for i in range(1, len(data)):
        current_data = data[i]
        previous_data = data[i - 1]
        data[0]['crossing'] = 0
        if current_data['EMA_ST'] > current_data['EMA_LT'] and previous_data['EMA_ST'] <= previous_data['EMA_LT']:
            data[i]['crossing'] = 1
        elif current_data['EMA_ST'] < current_data['EMA_LT'] and previous_data['EMA_ST'] >= previous_data['EMA_LT']:
            data[i]['crossing'] = -1
        else:
            data[i]['crossing'] = 0
    return data



# # Example data as a list of dictionaries
# data = [
#     {'Date': '2023-07-28', 'Close_price': 1, 'EMA_LT': 1, 'EMA_ST': 0},
#     {'Date': '2023-07-29', 'Close_price': 3, 'EMA_LT': 3, 'EMA_ST': 5},
#     {'Date': '2023-07-30', 'Close_price': 5, 'EMA_LT': 5, 'EMA_ST': 4},
#     {'Date': '2023-07-31', 'Close_price': 7, 'EMA_LT': 7, 'EMA_ST': 20},
#     {'Date': '2023-08-01', 'Close_price': 9, 'EMA_LT': 9, 'EMA_ST': 20}
# ]

# # Detect crossings
# crossings = crossing(data)
# print(crossings[:5])

