import streamlit as st
import pandas as pd
import pickle

# Page Config
st.set_page_config(
    page_title="Lead Quality Predictor",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Sales Lead Quality Predictor")
st.write("Upload your sales lead dataset and predict lead status.")

# Load Model
@st.cache_resource
def load_model():
    with open("lead_quality_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# File Upload
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())

    # Data Cleaning
    df.fillna("Unknown", inplace=True)

    st.subheader("Lead Source Distribution")

    if "Source" in df.columns:
        st.bar_chart(df["Source"].value_counts())

    st.subheader("Lead Status Distribution")

    if "Status" in df.columns:
        st.bar_chart(df["Status"].value_counts())

    # Prediction Section
    st.subheader("Lead Prediction")

    feature_columns = [
        "Source",
        "Sales_Agent",
        "Location",
        "Delivery_Mode"
    ]

    if all(col in df.columns for col in feature_columns):

        X = df[feature_columns]

        predictions = model.predict(X)

        df["Predicted_Status"] = predictions

        st.success("Prediction Completed Successfully")

        st.dataframe(
            df[
                [
                    "Created",
                    "Source",
                    "Sales_Agent",
                    "Delivery_Mode",
                    "Predicted_Status"
                ]
            ]
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Predictions",
            data=csv,
            file_name="lead_predictions.csv",
            mime="text/csv"
        )

    else:
        st.error(
            f"Required columns missing: {feature_columns}"
        )

else:
    st.info("Please upload a CSV file to begin.")