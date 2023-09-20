import requests

#THIS DATA NEEDS TO BE rETRIEVED ONCE ONLY!

def get_data_from_binance(coin, interval, start, end): #no limit argument here
    url = f"https://api.binance.com/api/v3/klines?symbol={coin}&interval={interval}&startTime={start}&endTime={end}"

    # print("this is url for fetching dataa on Binance API - this is a def print", url)
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    get_data_from_binance("BTCUSDT", "1d", 1688659458000, 1693841547000)

