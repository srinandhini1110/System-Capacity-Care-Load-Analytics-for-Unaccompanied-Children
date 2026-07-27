import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------
st.set_page_config(
    page_title="System Capacity & Care Load Analytics",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.title("📊 System Capacity & Care Load Analytics for Unaccompanied Children")

st.markdown("""
This interactive dashboard analyzes the **HHS Unaccompanied Children Program**
to understand operational trends in:

- Children in HHS Care
- Children Apprehended
- Children Discharged
- Capacity Planning
- Care Load Analysis
""")

st.divider()

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
try:
    df = pd.read_csv("data/cleaned_data.csv")

    df.rename(columns={
        "Children apprehended and placed in CBP custody*":
        "Children apprehended and placed in CBP custody"
    }, inplace=True)

    df["Date"] = pd.to_datetime(df["Date"])

    # Sort for clean graphs
    df = df.sort_values("Date")

except Exception as e:
    st.error(f"Unable to load dataset.\n\n{e}")
    st.stop()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("📅 Filters")

years = sorted(df["Year"].unique())

selected_years = st.sidebar.multiselect(
    "Select Year",
    options=years,
    default=years
)

filtered_df = df[df["Year"].isin(selected_years)]

st.sidebar.markdown("---")
st.sidebar.write(f"Records : **{len(filtered_df)}**")

# -------------------------------------------------
# KEY METRICS
# -------------------------------------------------
st.header("📈 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average HHS Care",
    f"{int(filtered_df['Children in HHS Care'].mean()):,}"
)

col2.metric(
    "Average Apprehensions",
    f"{int(filtered_df['Children apprehended and placed in CBP custody'].mean()):,}"
)

col3.metric(
    "Average Discharges",
    f"{int(filtered_df['Children discharged from HHS Care'].mean()):,}"
)

st.divider()

# -------------------------------------------------
# HHS CARE
# -------------------------------------------------
st.subheader("Children in HHS Care")

fig, ax = plt.subplots(figsize=(12,4))

ax.plot(
    filtered_df["Date"],
    filtered_df["Children in HHS Care"],
    linewidth=2
)

ax.set_xlabel("Date")
ax.set_ylabel("Children")

st.pyplot(fig)

# -------------------------------------------------
# APPREHENSIONS
# -------------------------------------------------
st.subheader("Children Apprehended")

fig, ax = plt.subplots(figsize=(12,4))

ax.plot(
    filtered_df["Date"],
    filtered_df["Children apprehended and placed in CBP custody"],
    linewidth=2
)

ax.set_xlabel("Date")
ax.set_ylabel("Children")

st.pyplot(fig)

# -------------------------------------------------
# DISCHARGES
# -------------------------------------------------
st.subheader("Children Discharged")

fig, ax = plt.subplots(figsize=(12,4))

ax.plot(
    filtered_df["Date"],
    filtered_df["Children discharged from HHS Care"],
    linewidth=2
)

ax.set_xlabel("Date")
ax.set_ylabel("Children")

st.pyplot(fig)

st.divider()

# -------------------------------------------------
# DATASET PREVIEW
# -------------------------------------------------
st.subheader("Dataset Preview")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)

# -------------------------------------------------
# SUMMARY
# -------------------------------------------------
st.subheader("Project Summary")

st.markdown("""
This dashboard provides insights into:

- Historical HHS care trends
- Apprehension patterns
- Discharge trends
- Capacity planning
- Operational workload

The dashboard enables quick exploration of yearly trends and supports
data-driven decision-making.
""")

# -------------------------------------------------
# DOWNLOAD DATA
# -------------------------------------------------
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_hhs_data.csv",
    mime="text/csv"
)

st.markdown("---")

st.caption(
    "Developed by Sri Nandhini Murali | Data Analytics Internship Project"
)
