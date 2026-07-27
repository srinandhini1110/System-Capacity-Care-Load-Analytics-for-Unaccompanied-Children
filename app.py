import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="System Capacity & Care Load Analytics", layout="wide")

st.title("System Capacity & Care Load Analytics for Unaccompanied Children")

# Load data
df = pd.read_csv("data/cleaned_data.csv")

df = df.rename(columns={
    "Children apprehended and placed in CBP custody*":
    "Children apprehended and placed in CBP custody"
})

df["Date"] = pd.to_datetime(df["Date"])

# Sidebar
st.sidebar.title("Filters")

years = sorted(df["Year"].unique())

selected_years = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

df = df[df["Year"].isin(selected_years)]

st.header("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average HHS Care",
    int(df["Children in HHS Care"].mean())
)

col2.metric(
    "Average Apprehensions",
    int(df["Children apprehended and placed in CBP custody"].mean())
)

col3.metric(
    "Average Discharges",
    int(df["Children discharged from HHS Care"].mean())
)

st.divider()

st.subheader("Children in HHS Care Over Time")

fig, ax = plt.subplots(figsize=(12,4))
ax.plot(df["Date"], df["Children in HHS Care"])
ax.set_xlabel("Date")
ax.set_ylabel("Children")
st.pyplot(fig)

st.subheader("Children Apprehended")

fig, ax = plt.subplots(figsize=(12,4))
ax.plot(df["Date"], df["Children apprehended and placed in CBP custody"])
ax.set_xlabel("Date")
ax.set_ylabel("Children")
st.pyplot(fig)

st.subheader("Children Discharged")

fig, ax = plt.subplots(figsize=(12,4))
ax.plot(df["Date"], df["Children discharged from HHS Care"])
ax.set_xlabel("Date")
ax.set_ylabel("Children")
st.pyplot(fig)

st.subheader("Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)
