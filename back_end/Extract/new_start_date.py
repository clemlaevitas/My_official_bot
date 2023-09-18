def match_EMAs_length(start_date,number, period):
    number = number - 1 #temporary
    if period == "1d":
        new_date = start_date - number * 86400 * 1000
        return new_date
    elif period == "1h":
        new_date = start_date - number * 3600 * 1000
        return new_date
    elif period == "1m":
        new_date = start_date - number * 60 * 1000
        return new_date