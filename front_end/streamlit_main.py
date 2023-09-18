import streamlit as st
import datetime
import requests

st.title("Prototype conditions")

def main():
    with st.form(f"EMA"):
        st.subheader("EMA")
        c3, c4= st.columns(2)
        c3.date_input("start_date", datetime.date(2022,8,1), key= 'start_date') #look if you could input a specific hour
        c4.date_input("end_date", datetime.datetime.now(), key= 'end_date')
        c1, c2 = st.columns(2)
        c1.selectbox("period", options = ['1d','1h','1m'], key = 'period') 
        c2.number_input("smoothing factor", value = 2, key = 'smooth')
        c5, c6 = st.columns(2)
        c5.selectbox("frequency_LT", [50,100,200], key = 'frequencyLT')
        c6.selectbox("frequency_ST", [5,10,20], key = 'frequencyST')

        btn1 = st.form_submit_button("Submit")

    if btn1:
        error_flag = False 
        if st.session_state['start_date'] > st.session_state['end_date']:
            st.error('Error: start_date is after end_date.')
            error_flag = True
        
        if st.session_state['period'] == '1m':
            st.error('Error: need to be further worked on for this granularity option.')
            error_flag = True
        
        delta = st.session_state['end_date'] - st.session_state['start_date']
        if delta.days + st.session_state['frequencyLT'] > 500:
            st.error('Error: Binance API cannot fetch that much data, max 500')
            error_flag = True
        if not error_flag:
            st.write('EMA parameters are submitted/updated')


    with st.form(f"Keltner Channels"):
        st.subheader("Keltner Channels")
        c7, c8 = st.columns(2)
        c7.selectbox("Middle band", ['EMA', 'SMA'], disabled = True, key = 'middle')
        c8.number_input("Period", step=5, key = 'periodKC', value = 200)
        c9, c10 = st.columns(2)
        c9.selectbox("ATR", ['1', '2', '3'], key = 'ATR') #to change
        c10.number_input("Nmber ATR/Multiplier", step=1, key = 'numberATR', value = 1)

        btn2 = st.form_submit_button("Submit")

    if btn2:
        st.write('Keltner Channels parameters are submitted/updated')

    all_conditions = st.button("Confirmation to store all conditions")

    if all_conditions:
        st.session_state['all_conditons'] = {}
        st.session_state['all_conditons']['EMA'] = {'start_date': st.session_state['start_date'],
            'end_date': st.session_state['end_date'],
            'period': st.session_state['period'],           
            'smoothing_factor': st.session_state['smooth'],
            'frequency_LT': st.session_state['frequencyLT'],
            'frequency_ST': st.session_state['frequencyST']}
        
        st.session_state['all_conditons']['Keltner Channels'] = {'middle_band': st.session_state['middle'],
            'period': st.session_state['periodKC'],
            'formula_ATR': st.session_state['ATR'],
            'number_ATR': st.session_state['numberATR']}
        
        st.write('these are all conditions that are stored in session state', st.session_state['all_conditons'])

    #QUErIES 

    #1) request for OHLC
    start_date = st.session_state['start_date']
    end_date = st.session_state['end_date']
    period = st.session_state['period']
    unix_start_date = int(datetime.datetime(start_date.year, start_date.month, start_date.day).timestamp()) #to unix, could be also in the back-end
    unix_end_date = int(datetime.datetime(end_date.year, end_date.month, end_date.day).timestamp())
    unix_start_date, unix_end_date = unix_start_date*1000, unix_end_date*1000


    url_OHLC = f'http://127.0.0.1:5000/EMA?start_date={unix_start_date}&end_date={unix_end_date}&period={period}'
    HTML_req1 = requests.get(url_OHLC)
    req1_result = HTML_req1.json()

    #... should return a dictionary { chart: "OHLC", OHLC: [list of dictionaries time series] }

    #2) request for EMAs and signals 
    smoothing_factor = st.session_state['smooth']
    frequency_LT = st.session_state['frequencyLT']
    frequency_ST = st.session_state['frequencyST']
    url_EMA = f'http://127.0.0.1:5000/EMA?start_date={unix_start_date}&end_date={unix_end_date}&smoothing_factor={smoothing_factor}&period={period}&frequLT={frequency_LT}&frequST={frequency_ST}'
    HTML_req2 = requests.get(url_EMA)
    req2_result = HTML_req2.json()

    #... should return a dictionary { chart: "EMA and signals", EMA: [list of dictionaries time series], signals: [list of dictionaries time series]}

    #3) request for Keltner Channels
    #todo later

if __name__ == "__main__":
    main()