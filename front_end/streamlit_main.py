import streamlit as st
import datetime
import requests
import plotly.graph_objects as go


st.title("Prototype conditions")

def main():
    with st.form(f'Date selection'):
        st.subheader("Date selection")
        c1, c2 = st.columns(2)
        c1.date_input("start_date", datetime.date(2021,8,1), key= 'start_date')
        c2.date_input("end_date", datetime.datetime.now(), key= 'end_date')
        st.selectbox("period", options = ['1d','1h','1m'], key = 'period') 

        btn1 = st.form_submit_button("Submit")

    if btn1: 
        if st.session_state['start_date'] > st.session_state['end_date']:
            st.error('Error: start_date is after end_date.')
            error_flag = True
        else:
            st.write('EMA parameters are submitted/updated')

    with st.form(f"EMA"):
        st.subheader("EMA")
        st.number_input("smoothing factor", value = 2, key = 'smooth')
        c3, c4 = st.columns(2)
        c3.selectbox("frequency_LT", [50,100,200], key = 'frequencyLT')
        c4.selectbox("frequency_ST", [5,10,20], key = 'frequencyST')

        btn2 = st.form_submit_button("Submit")

    if btn2:
        error_flag = False
        limit = 500 #to change dependtly on API
        delta = st.session_state['end_date'] - st.session_state['start_date']

        if st.session_state['period'] == '1m':
            st.error('Error: need to be further worked on for this granularity option.')
            error_flag = True
        elif st.session_state['period'] == '1h':
            ammount = delta.seconds // 3600
        elif st.session_state['period'] == '1d':
            ammount = delta.days
       
        if ammount + st.session_state['frequencyLT'] > limit:
            st.error(f'Error: Binance API cannot fetch that much data, max {limit}')
            error_flag = True
        if ammount < st.session_state['frequencyLT']:
            st.error('Error: frequency_LT is too high for the selected period')
            error_flag = True
        if not error_flag:
            st.write('EMA parameters are submitted/updated')
        #verify if have to modify period simultaneously
    
    with st.form(f"Keltner Channels"):
        st.subheader("Keltner Channels")
        c7, c8 = st.columns(2)
        c7.selectbox("Middle band", ['EMA', 'SMA'], disabled = True, key = 'middle')
        c8.number_input("Period", step=5, key = 'periodKC', value = 200)
        c9, c10 = st.columns(2)
        c9.selectbox("ATR", ['1', '2', '3'], key = 'ATR') #to change
        c10.number_input("Nmber ATR/Multiplier", step=1, key = 'numberATR', value = 1)

        btn3 = st.form_submit_button("Submit")

    if btn3:
        st.write('Keltner Channels parameters are submitted/updated')

    
    all_conditions = st.button("Confirmation to store all conditions") #let not run it if error to do

    if all_conditions:
        st.session_state['all_conditons'] = {}
        st.session_state['all_conditons']['Date'] = {'start_date': st.session_state['start_date'], 'end_date': st.session_state['end_date']}
        st.session_state['all_conditons']['EMA'] = {
            'period': st.session_state['period'],           
            'smoothing_factor': st.session_state['smooth'],
            'frequency_LT': st.session_state['frequencyLT'],
            'frequency_ST': st.session_state['frequencyST']}
        st.session_state['all_conditons']['Keltner Channels'] = {'middle_band': st.session_state['middle'],
            'period': st.session_state['periodKC'],
            'formula_ATR': st.session_state['ATR'],
            'number_ATR': st.session_state['numberATR']}
            #change parmaeters here!!
        
        st.write('these are all conditions that are stored in session state', st.session_state['all_conditons'])

#     #QUErIES

        
    start_date = st.session_state['start_date']
    end_date = st.session_state['end_date']
    period = st.session_state['period']

    smoothing_factor = st.session_state['smooth']
    frequency_LT = st.session_state['frequencyLT']
    frequency_ST = st.session_state['frequencyST']
    

    if all_conditions:
        #1) request for OHLC
        url_OHLC = f'http://127.0.0.1:5000/OHLC?start_date={start_date}&end_date={end_date}&period={period}'
        HTML_req1 = requests.get(url_OHLC)
        OHLC_data = HTML_req1.json()
        st.write('this is OHLC_data', OHLC_data)

        # 2) request for EMAs and signals 
        smoothing_factor = st.session_state['smooth']
        frequency_LT = st.session_state['frequencyLT']
        frequency_ST = st.session_state['frequencyST']
        url_EMA = f'http://127.0.0.1:5000/EMA?start_date={start_date}&end_date={end_date}&smoothing_factor={smoothing_factor}&period={period}&frequLT={frequency_LT}&frequST={frequency_ST}'
        HTML_req2 = requests.get(url_EMA)
        req2_result = HTML_req2.json()
        st.write('this is req2_result', req2_result)

    #     #should return a dictionary { chart: "EMA and signals", EMA: [list of dictionaries time series], signals: [list of dictionaries time series]}

    #     #3) request for Keltner Channels
    #     #todo later

#Visualisation

        fig1 = go.Figure()
        trace = go.Candlestick(
            x = [elem['Date'] for elem in OHLC_data['OHLC']],
            open = [elem['Open_price'] for elem in OHLC_data['OHLC']],
            high = [elem['High_price'] for elem in OHLC_data['OHLC']],
            low = [elem['Low_price'] for elem in OHLC_data['OHLC']],
            close = [elem['Close_price'] for elem in OHLC_data['OHLC']]
        )
        fig1.update_layout(title='EMAs, KC and candlestick', xaxis_title='Date', yaxis_title='EMA, candlestick', xaxis_rangeslider_visible=False)

        fig1.add_trace(trace)
        st.write(fig1)

        fig2 = go.Figure()
        x = [elem['Date'] for elem in req2_result['EMA_and_signals']]
        y1 = [elem['EMALT'] for elem in req2_result['EMA_and_signals']]
        y2 = [elem['EMA_ST'] for elem in req2_result['EMA_and_signals']]
        
        fig2.add_trace(go.Scatter(x=x, y=y1, name = 'LT'))
        fig2.add_trace(go.Scatter(x=x, y=y2, name = 'ST'))

        fig2.update_layout(title='EMAs', xaxis_title='Date', yaxis_title='EMA', xaxis_rangeslider_visible=False)
        #signals with crossings key
        st.write(fig2)

if __name__ == "__main__":
    main()
