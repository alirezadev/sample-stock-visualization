import streamlit as st
import yfinance as fi
from PIL import Image
import datetime

st.write('''
# FINANCE

this is a sample **stock** visualization 

''')

if 'visibility' not in st.session_state:
    st.session_state['visibility'] = 'visible'
    st.session_state['disabled'] = False

img = Image.open("C:/Users/jacka/Pictures/sample_chart.png")
# img = Image.open("./sample_chart.png")
st.image(img, caption='make life better')

crypto_symbol = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'ADA-USD', 'SOL-USD', 'DOGE-USD', 'MATIC-USD', 'ATOM-USD', 'DOT-USD']

sel_symbol = st.sidebar.selectbox('Select your Symbol', crypto_symbol, key="placeholder",
                                  disabled=st.session_state.disabled)
ck = st.sidebar.checkbox('Use Custom Symbol', key="disabled")
custom_symbol = st.sidebar.text_input('Enter your symbol',
                                      placeholder=st.session_state.placeholder,
                                      help='''
                                      Crypto : _TRX-USD, AVAX-USD, LINK-USD, etc.._
                                      Stocks : _GOOG, AAPL, AMZN, TSLA, UBER, etc.._ ''')
if ck:
    symbol = custom_symbol
else:
    symbol = sel_symbol
# Created by Alireza MohammadpourShahkolaei
START = st.sidebar.date_input('Enter Start date', datetime.date(2019, 1, 1))
END = st.sidebar.date_input('Enter End date', min_value=START)

# st.write(f'start is {START} and end is {END} symbol = {symbol}')
data = fi.Ticker(symbol)
history = data.history(period="1d", start=START, end=END)

st.header('PRICE')
st.write(symbol)
st.line_chart(history.Close)
st.header('VOLUME')
st.write(symbol)
st.line_chart(history.Volume)
# Created by Alireza MohammadpourShahkolaei
