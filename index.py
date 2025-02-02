import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data_day = pd.read_csv("data_day.csv")
data_hour = pd.read_csv("data_hour.csv")

# Preprocessing data
data_day['season'] = data_day['season'].map({1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"})
data_hour['season'] = data_hour['season'].map({1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"})

# Dashboard title
st.title("Dashboard Bike Sharing")

# Sidebar options
st.sidebar.title("Filter Data")
season_filter = st.sidebar.multiselect("Select season:", options=data_day['season'].unique(), default=data_day['season'].unique())
day_filter = st.sidebar.multiselect("Select day:", options=data_day['weekday'].unique(), default=data_day['weekday'].unique())

# Filter data based on selections
filtered_data_day = data_day[data_day['season'].isin(season_filter) & data_day['weekday'].isin(day_filter)]

# Display filtered data
st.write("Data yang Ditampilkan:", filtered_data_day)

# Visualization
st.subheader("Jumlah Penyewaan Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(data=filtered_data_day, x='season', y='cnt', ax=ax)
plt.title("Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)
