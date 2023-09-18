#MONGODB ---------
# import pymongo
# my_client = pymongo.MongoClient("mongodb://localhost:27017/")

#PACKAGES ---------
from flask import Flask,request, jsonify #if needed
from datetime import datetime

from Transform.list_to_dict_ohlc import prepared_data
from Transform.date_conversions import datetime_to_unixtime #, unixtime_to_datetime
from Transform.multiple_queries import number_data_points, create_couples, fetch_data

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

    #so start_date - LT_frequency?? for matching lenght, but need to pass it as argument

    dict = {}
    dict["chart"] = "OHLC"
    dict["OHLC"] = data

    return dict #structure is fine

#---------------------------------------------------
# @app.route("/EMA")
# def get_ema_params_2():
#     smoothing_factor = int(request.args.get("smoothing_factor"))
#     frequency_LT = int(request.args.get("frequLT"))
#     frequency_ST = int(request.args.get("frequST"))

#     return EMA 

# @app.route("/KC")
# def get_ema_params_3():
#     #...
#     return KC


if __name__ == "__main__":
    app.run()
