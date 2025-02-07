###################################### Import libraries ############################################
import streamlit as st
import pandas as pd 
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static 
from keplergl import KeplerGl
from datetime import datetime as dt 
import streamlit.components.v1 as components


###################################### Page Configuration ############################################
st.set_page_config(page_title='New York CitiBike Dashboard', layout='wide')


####################################### Title and Description #########################################
st.title("🚴‍♀️ New York CitiBike Dashboard")
st.markdown("This dashboard visualizes New York CitiBike trips in 2022 along with weather trends from National Oceanic and Atmospheric Administration (NOAA).")


################# Import data ######################
df = pd.read_csv('reduced_data_to_plot.csv', index_col = 0)
top_20_stations = pd.read_csv('top20_stations.csv', index_col = 0)


################# Define the Charts ########################

###### Create the bar chart ######
fig = go.Figure(go.Bar(
    x=top_20_stations['start_station_name'], 
    y=top_20_stations['value'], 
    marker=dict(color=top_20_stations['value'], colorscale="blues")
    ))
# Customize layout
fig.update_layout(
    title=dict(
        text="Top 20 Most Popular CitiBike Stations in New York",
        x=0.5,  # Centers the title
        xanchor="center",
        yanchor="top"
    ),
    xaxis_title="Station Name",
    yaxis_title="Number of Trips",
    xaxis=dict(tickangle=-45),  # Rotate x-axis labels
    template="plotly_dark",  # Dark theme
    margin=dict(l=40, r=40, t=40, b=120)  # Adjust margins
)
st.plotly_chart(fig, use_container_width=True)


df['date'] = pd.to_datetime(df['date'])

###### Create the line chart ######
fig_1 = make_subplots(specs=[[{"secondary_y": True}]])

#Resample to weekly data
weekly_data = df.resample('W', on='date').agg({'trips_per_day': 'sum', 'avgTemp': 'mean'}).reset_index()

fig_1.add_trace(
    go.Scatter(x=weekly_data['date'], y=weekly_data['trips_per_day'], name='Daily Bike Rides'),
    secondary_y=False
)
fig_1.add_trace(
    go.Scatter(x=weekly_data['date'], y=weekly_data['avgTemp'], name='Daily Temperature',  line=dict(color='red')),
    secondary_y=True
)
fig_1.update_layout(
    title=dict(
        text='Bike Trips & Temperature Trends in New York',  # Title text
        x=0.5,                      # Centers the title horizontally
        xanchor='center',           # Anchor the title at the center
        yanchor='top'               # Keep the title aligned to the top
    ),
    height=600,
    legend=dict(orientation='h', x=0.5, y=-0.2, xanchor='center')
)
st.plotly_chart(fig_1, use_container_width=True)


############################# Add the map ##############################
path_to_html = "New York Citibike Trips Aggregated.html"

# Read the HTML file with UTF-8 encoding
with open(path_to_html, 'r', encoding='utf-8') as f: 
    html_data = f.read()

# Display the map with scrolling and defined width
st.header("Aggregated Citibike Trips in New York")
components.html(html_data, height=800, width=1200, scrolling=True)