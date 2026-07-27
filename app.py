import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="System Capacity & Care Load Analytics", layout="wide")

st.title("System Capacity & Care Load Analytics for Unaccompanied Children")

try:
    df = pd.read_csv("data/cleaned_data.csv")

    df = df.rename(columns={
        "Children apprehended and placed in CBP custody*":
        "Children apprehended and placed in CBP custody"
    })

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()