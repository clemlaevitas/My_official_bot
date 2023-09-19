from Transform.EMA.calc_EMA import calcul_ema #won't work same problem!!

#FOrMULA & PArAMETErS
# period (20 I think)
# atr_multiplier (2)

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

def calculate_atr(data, period):
    atr_values = []  # Store ATR values

    for i in range(len(data)):
        if i == 0:
            tr = data[i]['High'] - data[i]['Low']
        else:
            high_minus_low = data[i]['High'] - data[i]['Low']
            high_minus_prev_close = abs(data[i]['High'] - data[i - 1]['Close_price'])
            low_minus_prev_close = abs(data[i]['Low'] - data[i - 1]['Close_price'])
            tr = max(high_minus_low, high_minus_prev_close, low_minus_prev_close)

        if i < period:
            atr_values.append(tr)
        else:
            prior_atr = atr_values[i-1]
            atr = ((prior_atr * (period - 1)) + tr) / period
            atr_values.append(atr)

    return atr_values


def calculate_keltner_channels(data, period, atr_period, atr_multiplier): #in data high, low and close, EMA
    ema_values = calcul_ema(data, period)  # Calculate EMA of Close_price, check if specific period!!!
    atr_values = calculate_atr(data, atr_period)  # Calculate ATR OK

    #change structure below!!
    keltner_channels = []

    for i in range(len(data)):
        ema = ema_values[i]
        atr = atr_values[i]
        upper_channel = ema + atr_multiplier * atr
        lower_channel = ema - atr_multiplier * atr
        keltner_channels.append({
            'Date': data[i]['Date'],  # You may need to adjust the key for the date
            'Upper_Channel': upper_channel,
            'Lower_Channel': lower_channel,
            'Middle_Line': ema,
        })

    return keltner_channels

#Example ATr---------------
# sample_data = [
#     {'High': 50.25, 'Low': 49.75, 'Close_price': 50.0},
#     {'High': 51.0, 'Low': 50.25, 'Close_price': 50.75},
#     {'High': 50.5, 'Low': 49.75, 'Close_price': 50.25},
#     {'High': 51.0, 'Low': 50.25, 'Close_price': 50.5},
#     {'High': 51.5, 'Low': 50.75, 'Close_price': 51.25},
#     {'High': 51.25, 'Low': 50.5, 'Close_price': 51.0},
#     {'High': 51.5, 'Low': 50.75, 'Close_price': 51.25},
# ]

# period = 14  # Specify the period for the ATR calculation

# atr_values = calculate_atr(sample_data, period)
# print(atr_values)

# # Print the ATR values
# for i, atr in enumerate(atr_values):
#     print(f'Day {i + 1}: ATR = {atr}')
