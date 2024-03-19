import streamlit as st
import pandas as pd
import requests
from repo import get_crypto_price, get_crypto_info
st.header("hello world")

data_crypto = pd.read_csv("crypt_symbol.csv")
alfa = st.selectbox("Select a crypto", [""]+data_crypto["symbol"].to_list())

# getting all the details 
if(alfa != ""):
    price = get_crypto_price(alfa)
    st.write(f"The  Real price of {alfa} is $ {price}")
    # RETREVING OTHER DATA
    alfa_2 = get_crypto_info(alfa)
    #print(alfa_2)
    data_symbol = alfa_2['data'][alfa][0]['symbol'] #type: ignore
    st.write(data_symbol)
    st.subheader('Description')
    data_description = alfa_2['data'][alfa][0]['description'] #type:ignore
    st.write(data_description)
    # image
    data_image = alfa_2['data'][alfa][0]['logo'] #type:ignore
    st.image(data_image)

    # other info
    st.subheader('Tages')
    data_tags = alfa_2['data'][alfa][0]['tags'] #type:ignore
    st.write(data_tags)



# historical info
st.subheader("Historical data")
data_1  = pd.read_csv("history_crypto.csv")

select_crypto = st.selectbox("select crypto",data_1['crypto_history'])

if(select_crypto != ""):
    crypto_read = pd.read_csv("Top 100 Crypto Coins/{}.csv".format(select_crypto))
    st.dataframe(crypto_read)
    # plotting  data
    st.line_chart(crypto_read[['High', 'Low', 'Close']])
    # volume chart
    st.line_chart(crypto_read['Volume'])
