import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
import os

st.title('Personalised Singapore HDB Resale Price Predictor')

st.subheader("By Kenneth Lim")
st.write("[GitHub](https://github.com/Lzwk16) | [LinkedIn](https://www.linkedin.com/in/lzwk16/)")

st.markdown('Please input your values')

#input features for predictions
floor_area_sqm = st.number_input('Floor Area (SQM)', min_value=30, max_value=300)
remaining_lease = st.slider('Remaining Years of Lease', min_value=0, max_value=99)
mid = st.slider('Floor Number', min_value=0, max_value=51)
max_floor_lvl = st.slider('Maximum Floor Level', min_value=0, max_value=51)
flat_type = st.selectbox('Flat Type', ('1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI_GENERATION'))
mrt_nearest_distance = st.number_input('Distance to Nearest MRT Station (metres)', min_value=0, max_value=3544)
town = st.selectbox('Estate', ('ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 
                               'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST', 'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL', 
                               'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN'))
mature_est = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT MERAH', 'BUKIT TIMAH', 'CENTRAL AREA', 'CLEMENTI', 
                 'GEYLANG', 'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'QUEENSTOWN', 'SERANGOON', 
                 'TAMPINES', 'TOA PAYOH']
if town in mature_est:
    Mature_Estate = 1
else:
    Mature_Estate = 0

if st.button('Predict'):
    model_path = os.path.join(os.getcwd(), 'HDB_model_final.joblib')
    model = joblib.load(model_path)
    x = pd.DataFrame([[floor_area_sqm, remaining_lease, mid, max_floor_lvl, flat_type, town, Mature_Estate, mrt_nearest_distance]], 
                     columns=['floor_area_sqm', 'remaining_lease', 'mid', 'max_floor_lvl', 'flat_type', 'town', 'Mature_Estate',  'mrt_nearest_distance'])
    pred = model.predict(x)[0]
    st.markdown(f'### Predicted Resale Price of your HDB Flat is ${str(int(round(pred, -3)))}')
