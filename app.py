import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("lead_quality_model.pkl")

st.set_page_config(page_title="Smart Sales Opportunity Scoring", layout="centered")

st.title("🎯 Smart Sales Opportunity Scoring")
st.write("Predict whether a lead is High Potential or Low Potential")

# Inputs
sales_agent = st.selectbox(
    "Sales Agent",
    ['Sales-Agent-2','Sales-Agent-3','Sales-Agent-4',
     'Sales-Agent-5','Sales-Agent-6','Sales-Agent-7',
     'Sales-Agent-8','Sales-Agent-9','Sales-Agent-10',
     'Sales-Agent-11','Sales-Agent-12']
)

location = st.selectbox(
    "Location",
    ['Bangalore','Others','Trivandrum','Hyderabad',
     'Chennai','Uk','Usa','Delhi','Uae','Mumbai',
     'Kolkata','Singapore','Pune','Australia',
     'Europe','Malaysia']
)

delivery_mode = st.selectbox(
    "Delivery Mode",
    ['Mode-1','Mode-2','Mode-3','Mode-4','Mode-5']
)

source_clean = st.selectbox(
    "Lead Source",
    ['Live Chat','Call','Website','By Recommendation',
     'Customer Referral','Email','Existing Customer',
     'Us Website','Justdial','Campaign','Other',
     'Crm Form','Sms Campaign','Personal Contact']
)

is_international = st.selectbox(
    "International Lead",
    [0,1]
)

month = st.selectbox(
    "Month",
    [4,5,6,7,8,9,10,11]
)

day = st.slider(
    "Day",
    min_value=1,
    max_value=31,
    value=15
)

hour = st.slider(
    "Hour",
    min_value=0,
    max_value=23,
    value=12
)

if st.button("Predict Lead Quality"):

    input_df = pd.DataFrame({
        'Sales_Agent':[sales_agent],
        'Location':[location],
        'Delivery_Mode':[delivery_mode],
        'Source_Clean':[source_clean],
        'Is_International':[is_international],
        'Month':[month],
        'Day':[day],
        'Hour':[hour]
    })

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("🔥 High Potential Lead")
    else:
        st.error("⚠️ Low Potential Lead")