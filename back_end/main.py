#MONGODB ---------
# import pymongo
# my_client = pymongo.MongoClient("mongodb://localhost:27017/")

#PACKAGES ---------
from flask import Flask,request, jsonify #if needed
from datetime import datetime

from Extract.new_start_date import match_EMAs_length
from Extract.OHLC_route import OHLC_route
from Transform.EMA.calc_EMA import calcul_ema
from Transform.date_conversions import datetime_to_unixtime #, unixtime_to_datetime
from Transform.multiple_queries import number_data_points, create_couples, fetch_data
from Transform.EMA.cross_signals import crossing


#---------------------------------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! this is the main page <h1>NEED TO BE MODIFIED<h1>" #there are first prints idk


@app.route("/OHLC")
def get_ema_params_1(): #dunno if same function name or not?
    start_date = request.args.get("start_date")
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = request.args.get("end_date")
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    period = request.args.get("period")

    start_date = datetime_to_unixtime(start_date) #NOT *1000!!
    end_date = datetime_to_unixtime(end_date)

    datapoints = number_data_points(start_date, end_date, period)
    couples = create_couples(start_date, end_date, datapoints)
    data = fetch_data(couples, period)
    #maybe I could do OHLC route here?

    dict = {}
    dict["chart"] = "OHLC"
    dict["OHLC"] = data

    return dict #structure is fine

#---------------------------------------------------
@app.route("/EMA")
def get_ema_params_2():
    start_date = request.args.get("start_date") #no orignial data easier to work with freq int
    end_date = request.args.get("end_date")
    period = request.args.get("period")
    smoothing_factor = int(request.args.get("smoothing_factor"))
    frequency_LT = int(request.args.get("frequLT"))
    frequency_ST = int(request.args.get("frequST"))

    #for loop over the two frequencies
    updated_start_date = match_EMAs_length(start_date, frequency_LT, period) #Here first time date modified
    data = OHLC_route(updated_start_date, end_date, period,only_closing_price=True) #only fetchingclosing price with the only_closing_price boolean

    EMA_LT = calcul_ema(data, frequency_LT, frequency_LT, smoothing_factor)
    EMA_ST_and_LT = calcul_ema(data, frequency_LT, frequency_ST, smoothing_factor)
    #EMA_LT not used, I could do fuction to merge both dictionries (more lean), but now it is automatically done. Because data is the return of calc_EMA

    data = crossing(EMA_ST_and_LT)

    #structure
    dict = {}
    dict["chart"] = "EMA_and_signals"
    dict["EMA_and_signals"] = data

    return data 

# @app.route("/KC")
# def get_ema_params_3():
#     #...
#     return KC


if __name__ == "__main__":
    app.run()
