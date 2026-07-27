import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="System Capacity", layout="wide")

st.title("System Capacity & Care Load Analytics for Unaccompanied Children")

st.write("✅ App Started")

try:
    df = pd.read_csv("data/cleaned_data.csv")
    st.write("✅ CSV Loaded")

    df = df.rename(columns={
        "Children apprehended and placed in CBP custody*":
        "Children apprehended and placed in CBP custody"
    })

    st.write("Columns:", list(df.columns))

    df["Date"] = pd.to_datetime(df["Date"])
    st.write("✅ Date Converted")

    st.write(df.head())

except Exception as e:
    st.error(e)
    st.stop()
