#need a list of dict with date!! take it maybe from OHLC

# def calcul_ema(data, frq_LT, frequ_ST, smoothing_factor): #what I should do

def calcul_ema(data, frq_period, smoothing_factor):
    smoothing = smoothing_factor / (1 + frq_period) 

    #initial EMA
    ema_sum = 0
    for i in range(frq_period):
        ema_sum += data[i]['Close_price']

        data[i]['EMA'] = float('nan') #facultative
    initial_ema = ema_sum / frq_period
        
    data[frq_period-1]['EMA'] = initial_ema
    ema_day_before = initial_ema

    #compute it
    for i in range(frq_period, len(data)):
        close_price = data[i]['Close_price']
        ema_value = (smoothing * close_price) + ((1 - smoothing) * ema_day_before) #ema_day_before
        ema_day_before = ema_value
        #append it to the existing dictionary
        data[i]['EMA'] = ema_value

    #ADD HErE TO KEEP ONLY FrOM THE STArT DATE!!! for both emas

    return data #need in the end a list of dictioanries 



# data_example = [{'Date': '2023-07-07', 'Open Price': 29895.42, 'High Price': 30449.0, 'Low Price': 29701.02, 'Close_price': 30344.7, 'Volume': 34070.53895}, {'Date': '2023-07-08', 'Open Price': 30344.7, 'High Price': 30386.81, 'Low Price': 30044.47, 'Close_price': 30284.63, 'Volume': 13094.59042}, {'Date': '2023-07-09', 'Open Price': 30284.63, 'High Price': 30445.52, 'Low Price': 30061.12, 'Close_price': 30160.71, 'Volume': 15388.50196}, {'Date': '2023-07-08', 'Open Price': 30344.7, 'High Price': 30386.81, 'Low Price': 30044.47, 'Close_price': 30284.63, 'Volume': 13094.59042}, {'Date': '2023-07-09', 'Open Price': 30284.63, 'High Price': 30445.52, 'Low Price': 30061.12, 'Close_price': 30160.71, 'Volume': 15388.50196}, {'Date': '2023-07-08', 'Open Price': 30344.7, 'High Price': 30386.81, 'Low Price': 30044.47, 'Close_price': 30284.63, 'Volume': 13094.59042}, {'Date': '2023-07-09', 'Open Price': 30284.63, 'High Price': 30445.52, 'Low Price': 30061.12, 'Close_price': 30160.71, 'Volume': 15388.50196}]
# if __name__ == "__main__":
#     calcul_ema(data_example, 3, 2)
#     #print(data_example)