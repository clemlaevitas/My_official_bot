#QUESTIONS: 
# - HOW SHOULD I STOrE THE OHLC DATA, IN A VArIABLE?
# - THINK ABOUT FOrMAT I WILL USE FOr DATE IN ALL CODE, when transforming it?
# - WHAT do I want to store in database, maybe all data OHLC and update it, only signals ect. What is NEXT, automated tradebot??
# - make a list of urls to call it together? OK

# - should I organize it like ETL? or services, send ,save?
# - put on Github for myself
# - how to order my folders

#Main only calling functions
#Function to Extract data (API), Transform data (in dict and EMA/KChannels +  call the API multiple times in definitions format), and Load data (on database and send rquests back)

#MONGODB ---------
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
# from pages.basic_mongodb import mongo

#PACKAGES ---------
from flask import Flask,request
# from pages.calcul_EMA import calcul_ema
# from pages.data_preparation import prepare_data_for_EMA
# from pages.new_start_date import match_EMAs_length
# from pages.signals import compare_time_series

#---------------------------------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! this is the main page <h1>NEED TO BE MODIFIED<h1>"

@app.route("/OHLC")
def get_ema_params_1(): #dunno if same function name or not?
    start_date = int(request.args.get("start_date"))
    end_date = request.args.get("end_date")
    period = request.args.get("period")

    return OHLC


@app.route("/EMA")
def get_ema_params_2():
    smoothing_factor = int(request.args.get("smoothing_factor"))
    frequency_LT = int(request.args.get("frequLT"))
    frequency_ST = int(request.args.get("frequST"))

    return EMA 

@app.route("/KC")
def get_ema_params_3():
    #...
    return KC


if __name__ == "__main__":
    app.run()
