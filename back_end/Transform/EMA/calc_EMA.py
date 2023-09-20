def ema(data, frequ_ref, frequ_EMA, smoothing_factor):
    smoothing = smoothing_factor / (1 + frequ_EMA)
    ema_sum = 0
    if frequ_ref == frequ_EMA:
        key_name = 'EMA_LT' #here key need maybe to change for KC?
    elif frequ_ref != frequ_EMA:
        key_name = 'EMA_ST'

    for i in range(frequ_EMA):
        ema_sum += data[i]['Close_price']
        data[i][key_name] = float('nan') #facultative
    initial_ema = ema_sum / frequ_EMA

    data[frequ_EMA-1][key_name] = initial_ema #to check the minus one
    ema_day_before = initial_ema

    for i in range(frequ_EMA, len(data)):
        close_price = data[i]['Close_price']
        ema_value = (smoothing * close_price) + ((1 - smoothing) * ema_day_before) #ema_day_before
        ema_day_before = ema_value
        #append it to the existing dictionary
        data[i][key_name] = ema_value

    return data #never smart to output the same variable name as input
    

def calcul_ema(data, frequ_ref, frequ_EMA, smoothing_factor = 2):

    if frequ_ref == frequ_EMA:
        data = ema(data, frequ_ref, frequ_EMA, smoothing_factor)

    elif frequ_ref > frequ_EMA:
        #remove the first (frequ_ref - frequ_EMA) elements from the list of dict
        data = data[frequ_ref - frequ_EMA:]
        #print the first date in the list of dict
        data = ema(data, frequ_EMA, smoothing_factor, frequ_ref)

    # data = data[frequ_EMA-1:] #remove nan values TO CHANGE!! and other keys

    return data #need in the end a list of dictioanries 
