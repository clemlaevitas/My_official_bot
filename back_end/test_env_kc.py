from Transform.EMA.calc_EMA import calcul_ema #only not works, same problem!!
#todo how to get the data OHLC route ect. imagine now the data

# I CHANGED CALC EMA§§§

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
    ema_values = calcul_ema(data, ema_period, ema_period)  #see arg function
    ema_values = [ema['EMA_LT'] for ema in ema_values] #change EMA_LT

    print('this is ema', len(ema_values))

    atr_values = calculate_atr(data, atr_period)
     
    print('this is atr', len(atr_values)) #not same length, changed it temporarly in def calc_EMA

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
#generated data
sample_data = [{'Date': '2023-01-01', 'High': 54.15, 'Low': 47.39, 'Close_price': 56.72}, {'Date': '2023-01-02', 'High': 59.28, 'Low': 49.71, 'Close_price': 50.51}, {'Date': '2023-01-03', 'High': 53.25, 'Low': 45.57, 'Close_price': 57.99}, {'Date': '2023-01-04', 'High': 52.26, 'Low': 47.35, 'Close_price': 49.11}, {'Date': '2023-01-05', 'High': 54.59, 'Low': 49.29, 'Close_price': 54.87}, {'Date': '2023-01-06', 'High': 59.86, 'Low': 48.63, 'Close_price': 50.94}, {'Date': '2023-01-07', 'High': 58.48, 'Low': 48.11, 'Close_price': 48.31}, {'Date': '2023-01-08', 'High': 58.38, 'Low': 48.14, 'Close_price': 54.77}, {'Date': '2023-01-09', 'High': 58.17, 'Low': 46.75, 'Close_price': 54.21}, {'Date': '2023-01-10', 'High': 53.17, 'Low': 48.86, 'Close_price': 54.4}, {'Date': '2023-01-11', 'High': 56.48, 'Low': 47.62, 'Close_price': 53.49}, {'Date': '2023-01-12', 'High': 57.55, 'Low': 45.59, 'Close_price': 56.36}, {'Date': '2023-01-13', 'High': 55.62, 'Low': 48.23, 'Close_price': 51.05}, {'Date': '2023-01-14', 'High': 57.19, 'Low': 47.24, 'Close_price': 50.71}, {'Date': '2023-01-15', 'High': 53.97, 'Low': 46.58, 'Close_price': 57.53}, {'Date': '2023-01-16', 'High': 52.2, 'Low': 49.93, 'Close_price': 49.73}, {'Date': '2023-01-17', 'High': 54.17, 'Low': 45.18, 'Close_price': 50.47}, {'Date': '2023-01-18', 'High': 60.0, 'Low': 48.93, 'Close_price': 49.76}, {'Date': '2023-01-19', 'High': 58.1, 'Low': 49.88, 'Close_price': 55.58}, {'Date': '2023-01-20', 'High': 57.98, 'Low': 49.34, 'Close_price': 49.76}, {'Date': '2023-01-21', 'High': 57.4, 'Low': 48.07, 'Close_price': 56.19}, {'Date': '2023-01-22', 'High': 54.16, 'Low': 47.42, 'Close_price': 53.12}, {'Date': '2023-01-23', 'High': 51.65, 'Low': 45.05, 'Close_price': 48.17}, {'Date': '2023-01-24', 'High': 53.86, 'Low': 45.07, 'Close_price': 53.62}, {'Date': '2023-01-25', 'High': 53.2, 'Low': 49.21, 'Close_price': 56.19}, {'Date': '2023-01-26', 'High': 58.86, 'Low': 46.36, 'Close_price': 52.45}, {'Date': '2023-01-27', 'High': 56.62, 'Low': 45.36, 'Close_price': 48.32}, {'Date': '2023-01-28', 'High': 50.52, 'Low': 45.34, 'Close_price': 51.11}, {'Date': '2023-01-29', 'High': 57.27, 'Low': 47.17, 'Close_price': 50.49}, {'Date': '2023-01-30', 'High': 57.48, 'Low': 47.43, 'Close_price': 55.69}, {'Date': '2023-01-31', 'High': 58.66, 'Low': 49.91, 'Close_price': 56.94}, {'Date': '2023-02-01', 'High': 59.98, 'Low': 49.16, 'Close_price': 54.79}, {'Date': '2023-02-02', 'High': 51.46, 'Low': 45.49, 'Close_price': 54.83}, {'Date': '2023-02-03', 'High': 54.73, 'Low': 47.56, 'Close_price': 57.61}, {'Date': '2023-02-04', 'High': 54.16, 'Low': 46.41, 'Close_price': 49.97}, {'Date': '2023-02-05', 'High': 54.12, 'Low': 45.73, 'Close_price': 49.78}, {'Date': '2023-02-06', 'High': 58.44, 'Low': 46.07, 'Close_price': 55.28}, {'Date': '2023-02-07', 'High': 59.48, 'Low': 47.31, 'Close_price': 48.91}, {'Date': '2023-02-08', 'High': 51.94, 'Low': 45.06, 'Close_price': 52.35}, {'Date': '2023-02-09', 'High': 59.56, 'Low': 49.95, 'Close_price': 57.41}, {'Date': '2023-02-10', 'High': 58.63, 'Low': 49.57, 'Close_price': 56.74}, {'Date': '2023-02-11', 'High': 54.04, 'Low': 46.24, 'Close_price': 57.44}, {'Date': '2023-02-12', 'High': 56.33, 'Low': 48.58, 'Close_price': 53.32}, {'Date': '2023-02-13', 'High': 56.32, 'Low': 47.77, 'Close_price': 52.52}, {'Date': '2023-02-14', 'High': 53.69, 'Low': 47.79, 'Close_price': 48.4}, {'Date': '2023-02-15', 'High': 50.2, 'Low': 45.69, 'Close_price': 50.47}, {'Date': '2023-02-16', 'High': 56.63, 'Low': 47.56, 'Close_price': 54.31}, {'Date': '2023-02-17', 'High': 54.79, 'Low': 49.69, 'Close_price': 56.4}, {'Date': '2023-02-18', 'High': 52.68, 'Low': 46.24, 'Close_price': 56.61}, {'Date': '2023-02-19', 'High': 55.12, 'Low': 46.64, 'Close_price': 48.62}, {'Date': '2023-02-20', 'High': 51.74, 'Low': 47.5, 'Close_price': 55.36}, {'Date': '2023-02-21', 'High': 56.4, 'Low': 47.11, 'Close_price': 55.53}, {'Date': '2023-02-22', 'High': 55.56, 'Low': 46.78, 'Close_price': 54.41}, {'Date': '2023-02-23', 'High': 56.63, 'Low': 45.42, 'Close_price': 52.9}, {'Date': '2023-02-24', 'High': 56.92, 'Low': 46.68, 'Close_price': 50.62}, {'Date': '2023-02-25', 'High': 59.4, 'Low': 48.56, 'Close_price': 48.73}, {'Date': '2023-02-26', 'High': 56.22, 'Low': 47.73, 'Close_price': 50.14}, {'Date': '2023-02-27', 'High': 57.45, 'Low': 46.19, 'Close_price': 56.07}, {'Date': '2023-02-28', 'High': 53.13, 'Low': 46.35, 'Close_price': 49.92}, {'Date': '2023-03-01', 'High': 54.28, 'Low': 49.29, 'Close_price': 54.98}, {'Date': '2023-03-02', 'High': 52.82, 'Low': 49.81, 'Close_price': 50.98}, {'Date': '2023-03-03', 'High': 57.67, 'Low': 49.6, 'Close_price': 55.61}, {'Date': '2023-03-04', 'High': 57.32, 'Low': 48.56, 'Close_price': 50.37}, {'Date': '2023-03-05', 'High': 58.56, 'Low': 46.86, 'Close_price': 56.18}, {'Date': '2023-03-06', 'High': 55.18, 'Low': 48.83, 'Close_price': 48.24}, {'Date': '2023-03-07', 'High': 55.42, 'Low': 45.97, 'Close_price': 53.64}, {'Date': '2023-03-08', 'High': 54.1, 'Low': 48.05, 'Close_price': 57.45}, {'Date': '2023-03-09', 'High': 53.44, 'Low': 46.57, 'Close_price': 50.58}, {'Date': '2023-03-10', 'High': 52.71, 'Low': 47.37, 'Close_price': 49.61}, {'Date': '2023-03-11', 'High': 55.78, 'Low': 45.64, 'Close_price': 48.65}, {'Date': '2023-03-12', 'High': 53.95, 'Low': 47.03, 'Close_price': 53.94}, {'Date': '2023-03-13', 'High': 57.95, 'Low': 47.72, 'Close_price': 48.98}, {'Date': '2023-03-14', 'High': 52.66, 'Low': 48.7, 'Close_price': 48.47}, {'Date': '2023-03-15', 'High': 56.11, 'Low': 48.87, 'Close_price': 55.39}, {'Date': '2023-03-16', 'High': 55.08, 'Low': 49.32, 'Close_price': 57.81}, {'Date': '2023-03-17', 'High': 51.64, 'Low': 49.63, 'Close_price': 53.47}, {'Date': '2023-03-18', 'High': 52.4, 'Low': 45.2, 'Close_price': 48.44}, {'Date': '2023-03-19', 'High': 50.2, 'Low': 49.87, 'Close_price': 51.36}, {'Date': '2023-03-20', 'High': 58.48, 'Low': 46.62, 'Close_price': 52.24}, {'Date': '2023-03-21', 'High': 53.75, 'Low': 45.79, 'Close_price': 53.87}, {'Date': '2023-03-22', 'High': 57.42, 'Low': 46.82, 'Close_price': 53.38}, {'Date': '2023-03-23', 'High': 51.23, 'Low': 45.71, 'Close_price': 50.83}, {'Date': '2023-03-24', 'High': 59.77, 'Low': 45.93, 'Close_price': 48.93}, {'Date': '2023-03-25', 'High': 52.92, 'Low': 45.97, 'Close_price': 48.68}, {'Date': '2023-03-26', 'High': 56.31, 'Low': 48.51, 'Close_price': 50.56}, {'Date': '2023-03-27', 'High': 53.78, 'Low': 49.6, 'Close_price': 53.4}, {'Date': '2023-03-28', 'High': 50.32, 'Low': 46.92, 'Close_price': 54.36}, {'Date': '2023-03-29', 'High': 55.08, 'Low': 49.83, 'Close_price': 53.74}, {'Date': '2023-03-30', 'High': 50.74, 'Low': 48.86, 'Close_price': 51.98}, {'Date': '2023-03-31', 'High': 53.91, 'Low': 49.16, 'Close_price': 54.37}, {'Date': '2023-04-01', 'High': 58.75, 'Low': 49.61, 'Close_price': 48.88}, {'Date': '2023-04-02', 'High': 51.54, 'Low': 48.77, 'Close_price': 55.14}, {'Date': '2023-04-03', 'High': 58.75, 'Low': 48.42, 'Close_price': 53.5}, {'Date': '2023-04-04', 'High': 54.14, 'Low': 46.17, 'Close_price': 49.85}, {'Date': '2023-04-05', 'High': 59.88, 'Low': 48.41, 'Close_price': 57.95}, {'Date': '2023-04-06', 'High': 52.29, 'Low': 48.15, 'Close_price': 55.68}, {'Date': '2023-04-07', 'High': 54.67, 'Low': 45.35, 'Close_price': 51.09}, {'Date': '2023-04-08', 'High': 58.78, 'Low': 47.39, 'Close_price': 49.08}, {'Date': '2023-04-09', 'High': 52.92, 'Low': 48.73, 'Close_price': 57.49}, {'Date': '2023-04-10', 'High': 56.54, 'Low': 48.9, 'Close_price': 54.76}]

result = calculate_keltner_channels(sample_data, ema_period, art_period, atr_multiplier)

#structure
dict = {}
dict["chart"] = "Keltner_channels"
dict["Keltner_channels"] = result

print(dict)
#It works!!!

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