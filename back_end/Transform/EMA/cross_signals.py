def compare_time_series(dates, values1, values2, type = 'EMA'):
    #could do some print statements
    crossings = []  # List to store crossing points

    if len(dates) != len(values1) or len(dates) != len(values2):
        raise ValueError("The length of the lists are not equal")
    else:
        pass

    for i in range(1, len(values1)):
        if values1[i] > values2[i] and values1[i - 1] <= values2[i - 1]:
            dict = {'type': type, 'date': dates[i], 'signal_direction': 1}
            crossings.append(dict) # append this like a dictionnary
        elif values1[i] < values2[i] and values1[i - 1] >= values2[i - 1]:
            dict = {'type': type, 'date': dates[i], 'signal_direction': -1}
            crossings.append(dict) 
    return crossings #list of dictionaries, fine
