import datetime
import pandas as pd
import yfinance as yf
import streamlit as st
import cufflinks as cf


def get_stock(name):
    stock_data = yf.Ticker(name)
    return stock_data


def app():
    st.title("A Simple APP for Checking Company's Stock Price")
    symbol_exist = False
    today_date = datetime.date.today()
    symbol_list = pd.read_csv('https://raw.githubusercontent.com/Michaelan171/s-and-p-500-companies/master/data'
                              '/constituents_symbols.txt')
    stock_name = st.text_input('Company Stock Symbol', value='GOOG').upper()
    for symbol in symbol_list['ABT']:
        if stock_name == symbol:
            symbol_exist = True
    if symbol_exist:
        stock = get_stock(stock_name)
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input('Start Date', datetime.date(2019, 1, 1))
        with col2:
            end_date = st.date_input('End Date', datetime.date(today_date.year, today_date.month, today_date.day))

        st.write('''---''')
        stock_df = stock.history(period='1d', start=start_date, end=end_date)
        stock_logo = '<img src=%s>' % stock.info['logo_url']
        st.markdown(stock_logo, unsafe_allow_html=True)

        stock_name = stock.info['longName']
        st.header('**%s**' % stock_name)

        stock_summary = stock.info['longBusinessSummary']
        st.info(stock_summary)

        st.header('**Ticker data**')
        st.write(stock_df)

        st.header('**Bollinger Bands**')
        qf = cf.QuantFig(stock_df, title='First Quant Figure', legend='top', name='GS')
        qf.add_bollinger_bands()
        fig = qf.iplot(asFigure=True)
        st.plotly_chart(fig)
    else:
        st.error('The symbol is not in the list. Please check following symbol list and try again.')
        st.write(symbol_list)

