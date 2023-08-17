import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import plotly.graph_objs as go
from streamlit_lottie import st_lottie

#import pandas.json_normalize
#from streamlit.web import StopException, RerunException
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

fig = go.Figure()
st.write("""# TECHNO verse""")

st.write("""
# Sentiments Analysis\U0001F603 \U0001F643 \U0001FAE0

""")
lottie_url = "https://lottie.host/af13b600-c618-4147-ad3c-ff77890331f8/S9YIHEDKf4.json"
lottie_json = load_lottieurl(lottie_url)
with st.sidebar:
    st_lottie(lottie_json)
st.write('Sentiment analysis is the interpretation and classification of emotions (positive, negative and neutral) within text data using text analysis techniques. Sentiment analysis tools allow businesses to identify customer sentiment toward products, brands or services in online feedback.                                          ')
st.set_option('deprecation.showfileUploaderEncoding', False)
st.sidebar.header('User Input(s)')
st.sidebar.subheader('Single Review Analysis')
single_review = st.sidebar.text_input('Enter single review below:')
st.sidebar.subheader('Mutiple Reviews Analysis')
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
count_positive = 0
count_negative = 0
count_neutral = 0
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    for i in range(input_df.shape[0]):
        url = 'https://aisentimentechnoverse-4582ec64764d.herokuapp.com/classify/?text='+str(input_df.iloc[i])
        
        r = requests.get(url)
        result = r.json()["text_sentiment"]
        if result=='positive':
            count_positive+=1
        elif result=='negative':
            count_negative+=1
        else:
            count_neutral+=1 

    x = ["Positive", "Negative", "Neutral"]
    y = [count_positive, count_negative, count_neutral]

    if count_positive>count_negative:
        st.write("""# Great Work there! Majority of people liked your product 😃""")
    elif count_negative>count_positive:
        st.write("""# Try improving your product! Majority of people didn't find your product upto the mark 😔""")
    else:
        st.write("""# Good Work there, but there's room for improvement! Majority of people have neutral reactions to your product 😶""")
        
    layout = go.Layout(
        title = 'Multiple Reviews Analysis',
        xaxis = dict(title = 'Category'),
        yaxis = dict(title = 'Number of reviews'),)
    
    fig.update_layout(dict1 = layout, overwrite = True)
    fig.add_trace(go.Bar(name = 'Multi Reviews', x = x, y = y))
    st.plotly_chart(fig, use_container_width=True)

elif single_review:
    url = 'https://aisentimentechnoverse-4582ec64764d.herokuapp.com/classify/?text='+single_review
    r = requests.get(url)
    result = r.json()["text_sentiment"]
    if result=='positive':
        st.write("""# Great Work there! You got a Positive Review 😃""")
    elif result=='negative':
        st.write("""# Try improving your product! You got a Negative Review 😔""")
    else:
        st.write("""# Good Work there, but there's room for improvement! You got a Neutral Review 😶""")

else:
    st.write("# ⬅ Enter user input from the sidebar to see the nature of the review.                                                                         ")

st.sidebar.subheader("""Created by Nullset """)

lottie_url_hello="https://lottie.host/d2d7c508-57ad-46ab-a98d-100f03f40cd2/NRvjkGp1M3.json"
lottie_img=load_lottieurl(lottie_url_hello)
st_lottie(lottie_img,key="hi")
