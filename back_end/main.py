#MONGODB ---------
# import pymongo
# my_client = pymongo.MongoClient("mongodb://localhost:27017/")

#PACKAGES ---------
from flask import Flask,request #jsonify if needed

from Extract.OHLC_fetching import OHLC_route
from Transform.EMA.calc_EMA import calcul_ema
from Transform.EMA.cross_signals import crossing
from Transform.KC.calc_KC import calculate_keltner_channels
from Load.structure import dict_structure

#---------------------------------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! this is the main page <h1>NEED TO BE MODIFIED<h1>" #there are first prints idk

@app.route("/OHLC")
def get_ema_params_1(): #dunno if same function name or not?
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    period = request.args.get("period")
    
    data = OHLC_route(start_date, end_date, period)
    responce_OHLC = dict_structure("OHLC", data)
 
    return responce_OHLC

@app.route("/EMA")
def get_ema_params_2():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    period = request.args.get("period")
    smoothing_factor = int(request.args.get("smoothing_factor"))
    frequency_LT = int(request.args.get("frequLT"))
    frequency_ST = int(request.args.get("frequST"))

    OHLC_data = OHLC_route(start_date, end_date, period, frequency_LT) #frequency_LT because here needed. Could try later only fetching closing price with the only_closing_price boolean

    EMA_LT = calcul_ema(OHLC_data, frequency_LT, frequency_LT, smoothing_factor)
    EMA_ST_and_LT = calcul_ema(OHLC_data, frequency_LT, frequency_ST, smoothing_factor)
    #EMA_LT not used, I could do fuction to merge both dictionries (more lean), but now it is automatically done. Because data is the return of calc_EMA

    data = crossing(EMA_ST_and_LT)

    response_EMA = dict_structure("EMA", data)

    return response_EMA 

@app.route("/KC")
def get_ema_params_3():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    period = request.args.get("period")
    ema_period = int(request.args.get("ema_period"))
    atr_period = int(request.args.get("atr_period"))
    atr_multiplier = float(request.args.get("atr_multiplier")) #or int

    OHLC_data = OHLC_route(start_date, end_date, period, ema_period) #check if correct, fetch more data with ema_period mark maybe as extra param

    result = calculate_keltner_channels(OHLC_data, ema_period, atr_period, atr_multiplier) #won't work with formula calc_ema because last line

    response_KC = dict_structure("KC", result)

    return response_KC



if __name__ == "__main__":
    app.run()
