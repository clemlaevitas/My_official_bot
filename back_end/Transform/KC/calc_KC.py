from Transform.EMA.calc_EMA import calcul_ema #won't work same problem!!
#todo how to get the data OHLC route ect. imagine now the data

#input: list of dict with date, high, low and close_price
#output: list of dictionaries with date, EMA, upper and lower channel (then you put it in a dict ok)

#FOrMULA & PArAMETErS
# data
atr_multiplier = 2
art_period = 10 #or 20 typically
ema_period = 20 #typically

def calculate_atr(data, atr_period):

    atr_values = []

    for i in range(len(data)):
        if i == 0:
            tr = data[i]['High'] - data[i]['Low']
        else:
            high_minus_low = data[i]['High'] - data[i]['Low']
            high_minus_prev_close = abs(data[i]['High'] - data[i - 1]['Close_price'])
            low_minus_prev_close = abs(data[i]['Low'] - data[i - 1]['Close_price'])
            tr = max(high_minus_low, high_minus_prev_close, low_minus_prev_close)

        if i < atr_period:
            atr_values.append(tr)
        else:
            prior_atr = atr_values[i-1]
            atr = ((prior_atr * (atr_period - 1)) + tr) / atr_period
            atr_values.append(atr)

    return atr_values #a simple list of atr values

def calculate_keltner_channels(data, ema_period, atr_period, atr_multiplier): 
    ema_values = calcul_ema(data, ema_period)  
    atr_values = calculate_atr(data, atr_period) 

    keltner_channels = []
    #before all lists (must be same length)

    for i in range(len(data)):
        ema = ema_values[i]
        atr = atr_values[i]
        upper_channel = ema + atr_multiplier * atr
        lower_channel = ema - atr_multiplier * atr
        keltner_channels.append({
            'Date': data[i]['Date'], 
            'Upper_Channel': upper_channel,
            'Lower_Channel': lower_channel,
            'Middle_Line': ema,
        })

    return keltner_channels


#Example ATr---------------
sample_data = [
    {'Date': '2023-01-01', 'High': 50.25, 'Low': 49.75, 'Close_price': 50.0},
    {'Date': '2023-01-02', 'High': 51.0, 'Low': 50.25, 'Close_price': 50.75},
    {'Date': '2023-01-03', 'High': 50.5, 'Low': 49.75, 'Close_price': 50.25},
    {'Date': '2023-01-04', 'High': 51.0, 'Low': 50.25, 'Close_price': 50.5},
    {'Date': '2023-01-05', 'High': 51.5, 'Low': 50.75, 'Close_price': 51.25},
    {'Date': '2023-01-06', 'High': 51.25, 'Low': 50.5, 'Close_price': 51.0},
    {'Date': '2023-01-07', 'High': 51.5, 'Low': 50.75, 'Close_price': 51.25},
    {'Date': '2023-01-08', 'High': 51.75, 'Low': 51.0, 'Close_price': 51.5},
    {'Date': '2023-01-09', 'High': 52.0, 'Low': 51.25, 'Close_price': 51.75},
    {'Date': '2023-01-10', 'High': 52.25, 'Low': 51.5, 'Close_price': 52.0},
    {'Date': '2023-01-11', 'High': 52.5, 'Low': 51.75, 'Close_price': 52.25},
    {'Date': '2023-01-12', 'High': 52.75, 'Low': 52.0, 'Close_price': 52.5},
    {'Date': '2023-01-13', 'High': 53.0, 'Low': 52.25, 'Close_price': 52.75},
]






# the formula for calculating the ATR:
#1) Calculate the true range (TR) for each data point:
#True Range (TR) = Max of the following three values:
    # High - Low (the range for the current period)
    # Absolute value of (High - Previous Close)
    # Absolute value of (Low - Previous Close)
#2) Calculate the first ATR!!! as a simple moving average (SMA) of the true range over the specified period.
#3) Calculate subsequent ATR values using an EMA formula:
# ATR = [(Prior ATR) * (n-1) + TR] / n
# Where n is the specified period for the ATR calculation.