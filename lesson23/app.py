import pandas as pd
import plotly.express as px
import streamlit as st

# Page config
st.set_page_config(page_title="City Sales Performance Dashboard", layout="wide")

st.title("📊 City Sales Performance Dashboard")
st.write(
    "This dashboard visualizes how product sales perform across different cities using the Advertising dataset."
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("lesson23/Advertising_F.csv")

df = load_data()

# Tabs or sections
tab1, tab2 = st.tabs(["Bar Plot (Average Sales)", "Scatter Plot (Geographic View)"])

with tab1:
    st.subheader("Average Sales by City")
    city_sales = df.groupby("City")["sales"].mean().reset_index().sort_values(by="sales", ascending=False)
    fig_bar = px.bar(
        city_sales,
        x="City",
        y="sales",
        labels={"sales": "Average Sales ($)", "City": "City"},
        color="sales",
        color_continuous_scale="Viridis",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    st.subheader("Geographic Distribution of Sales")
    fig_scatter = px.scatter(
        df,
        x="longitude",
        y="latitude",
        size="sales",
        color="sales",
        hover_name="City",
        labels={"sales": "Sales", "latitude": "Latitude", "longitude": "Longitude"},
        color_continuous_scale="Viridis",
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
