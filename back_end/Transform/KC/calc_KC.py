from Transform.EMA.calc_EMA import calcul_ema #won't work same problem!!

#input: list of dict with date, high, low and close_price
#output: list of dictionaries with date, EMA, upper and lower channel (then you put it in a dict ok)

def calculate_atr(data, atr_period):

    atr_values = []

    for i in range(len(data)):
        if i == 0:
            tr = data[i]['High_price'] - data[i]['Low_price']
        else:
            high_minus_low = data[i]['High_price'] - data[i]['Low_price']
            high_minus_prev_close = abs(data[i]['High_price'] - data[i - 1]['Close_price'])
            low_minus_prev_close = abs(data[i]['Low_price'] - data[i - 1]['Close_price'])
            tr = max(high_minus_low, high_minus_prev_close, low_minus_prev_close)

        if i < atr_period:
            atr_values.append(tr)
        else:
            prior_atr = atr_values[i-1]
            atr = ((prior_atr * (atr_period - 1)) + tr) / atr_period
            atr_values.append(atr)

    return atr_values #a simple list of atr values

def calculate_keltner_channels(data, ema_period, atr_period, atr_multiplier): 
    ema_values = calcul_ema(data, ema_period, ema_period) #to check again twice the same here to change when all 3 requests 

    ema_values = [ema['EMA_LT'] for ema in ema_values] #change structure of calc_ema to have only one key

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
            'KC_upper': upper_channel,
            'KC_lower': lower_channel,
            'KC_middle': ema,
        })

    return keltner_channels

