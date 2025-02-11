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
# st.set_page_config(page_title='New York CitiBike Dashboard', layout='wide')


####################################### Title and Description #########################################
# st.title("🚴‍♀️ New York CitiBike Dashboard")
# st.markdown("This dashboard visualizes New York CitiBike trips in 2022 along with weather trends from National Oceanic and Atmospheric Administration (NOAA).")


################# Import data ######################
df = pd.read_csv('reduced_data_to_plot.csv', index_col = 0)
top_20_stations = pd.read_csv('top20_stations.csv', index_col = 0)


################# Define the Charts ########################

###### Create the bar chart ######
# fig = go.Figure(go.Bar(
#    x=top_20_stations['start_station_name'], 
#   y=top_20_stations['value'], 
#    marker=dict(color=top_20_stations['value'], colorscale="blues")
#    ))
# Customize layout
# fig.update_layout(
#    title=dict(
#        text="Top 20 Most Popular CitiBike Stations in New York",
#        x=0.5,  # Centers the title
#        xanchor="center",
#        yanchor="top"
#    ),
#    xaxis_title="Station Name",
#    yaxis_title="Number of Trips",
#    xaxis=dict(tickangle=-45),  # Rotate x-axis labels
#    template="plotly_dark",  # Dark theme
#    margin=dict(l=40, r=40, t=40, b=120)  # Adjust margins
# )
# st.plotly_chart(fig, use_container_width=True)


###### Create the line chart ######

# df['date'] = pd.to_datetime(df['date'])
# fig_1 = make_subplots(specs=[[{"secondary_y": True}]])

# Resample to weekly data
# weekly_data = df.resample('W', on='date').agg({'trips_per_day': 'sum', 'avgTemp': 'mean'}).reset_index()

# fig_1.add_trace(
#    go.Scatter(x=weekly_data['date'], y=weekly_data['trips_per_day'], name='Daily Bike Rides'),
#    secondary_y=False
# )
# fig_1.add_trace(
#    go.Scatter(x=weekly_data['date'], y=weekly_data['avgTemp'], name='Daily Temperature', line=dict(color='red')),
#    secondary_y=True
# )

# fig_1.update_layout(
#    title=dict(
#        text='Bike Trips & Temperature Trends in New York',
#        x=0.5,
#        xanchor='center',
#        yanchor='top'
#    ),
#    height=600,
#    legend=dict(orientation='h', x=0.5, y=-0.2, xanchor='center')
# )

# Add axis labels
# fig_1.update_xaxes(title_text='Date')
# fig_1.update_yaxes(title_text='Number of Bike Rides', secondary_y=False)
# fig_1.update_yaxes(title_text='Average Temperature', secondary_y=True)

# st.plotly_chart(fig_1, use_container_width=True)



############################# Add the map ##############################
# path_to_html = "Updated_New_York_Citibike_Trips_Aggregated.html"

# Read the HTML file with UTF-8 encoding
# with open(path_to_html, 'r', encoding='utf-8') as f: 
#    html_data = f.read()

# Display the map with scrolling and defined width
# st.header("Most Common Citibike Trips in New York")
# components.html(html_data, height=800, width=1200, scrolling=True)

############################################################## PART 2 ###################################################################

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
from numerize.numerize import numerize
from PIL import Image

###################################### Initial Settings for the Dashboard #####################################

# Streamlit initial settings
st.set_page_config(page_title='CitiBike Strategy Dashboard', layout='wide')
st.title("CitiBike Strategy Dashboard")

# Define the sidebar for navigation
st.sidebar.title("Aspect Selector")
page = st.sidebar.selectbox('Select an aspect of the analysis',
    ["Intro page", 
     "Weather component and bike usage",
     "Most popular stations",
     "Interactive map with aggregated bike trips",
     "Boxplot for User Type",
     "Recommendations"])

df_1 = pd.read_csv('reduced_cleaned_citibike_data.csv', index_col = 0)

###### Intro page ######

if page == "Intro page":
    st.markdown("#### This dashboard provides strategic insights into the operational and supply challenges faced by New York Citi Bike in 2022.")
    st.markdown("""
    As the **lead analyst** for Citi Bike, this dashboard aims to support the **business strategy team** in evaluating the current **logistics model** and uncovering opportunities for expansion, based on 2022 data.  
    Citi Bike has seen significant growth since its launch in 2013, with ridership demand surging post-Covid-19. In 2022, this surge has led to challenges such as:
    - **Bike shortages** at high-demand stations  
    - **Docking issues** at overcrowded stations  
    - **Customer complaints** related to bike availability  
    
    To help address these issues, the dashboard is divided into 5 key sections:
    - 🌦️ **Weather Impact on Bike Usage**: Examining how weather conditions influenced ridership in 2022
    - 🚲 **Most Popular Stations**: Identifying areas with the highest demand in 2022    
    - 🗺️ **Interactive Map with Aggregated Bike Trips**: Visualizing the spatial distribution of trips in 2022  
    - 📊 **User Type Analysis (Boxplot)**: Comparing behaviors between members and casual riders in 2022  
    - ✅ **Recommendations**: Offering actionable strategies to enhance bike availability and distribution, based on 2022 trends  
    
    Use the **'Aspect Selector'** dropdown on the left to navigate through different sections of the analysis.
    """)

    from PIL import Image
    myImage = Image.open("Citi_Bike.jpg")  # Source: https://www.citibikenyc.com/
    st.image(myImage)


###### Duel Axis Line Chart Page ######

if page == "Weather component and bike usage":
    st.markdown("### 🌦️ Bike Trips & Temperature Trends in New York (2022)")

    # Add interpretation Markdown section
    st.markdown("""
    This chart illustrates the relationship between the number of daily bike rides and the average temperature in New York during 2022. 
    The data is resampled weekly, showing trends in bike ridership and temperature variations. 
    - The **blue line** represents the total number of bike rides per day.
    - The **red line** shows the average daily temperature.
    
    The chart allows us to analyze how temperature fluctuations correlate with bike usage patterns over time:
    - **Bike trips** generally increase as the weather warms up, especially during spring and summer months.
    - **Temperature spikes** are often followed by a noticeable rise in bike ridership.
    - On colder days, bike usage tends to drop, which is visible in the downward trends on the graph.

    This analysis helps us understand how external weather conditions can influence demand for bike sharing services and assists in optimizing bike distribution accordingly.
    """)

    # Create the line chart
    df['date'] = pd.to_datetime(df['date'])
    fig_1 = make_subplots(specs=[[{"secondary_y": True}]])

    # Resample to weekly data
    weekly_data = df.resample('W', on='date').agg({'trips_per_day': 'sum', 'avgTemp': 'mean'}).reset_index()

    fig_1.add_trace(
        go.Scatter(x=weekly_data['date'], y=weekly_data['trips_per_day'], name='Daily Bike Rides'),
        secondary_y=False
    )
    fig_1.add_trace(
        go.Scatter(x=weekly_data['date'], y=weekly_data['avgTemp'], name='Daily Temperature', line=dict(color='red')),
        secondary_y=True
    )

    fig_1.update_layout(
        title=dict(
            text='Bike Trips & Temperature Trends in New York',
            x=0.5,
            xanchor='center',
            yanchor='top'
        ),
        height=600,
        legend=dict(orientation='h', x=0.5, y=-0.2, xanchor='center')
    )

    # Add axis labels
    fig_1.update_xaxes(title_text='Date')
    fig_1.update_yaxes(title_text='Number of Bike Rides', secondary_y=False)
    fig_1.update_yaxes(title_text='Average Temperature', secondary_y=True)

    # Display the chart
    st.plotly_chart(fig_1, use_container_width=True)

###### Bar Chart for Most popular stations ######

if page == "Most popular stations":
    st.markdown("### 🚲 Top 20 Most Popular CitiBike Stations in New York (2022)")

    # Add interpretation Markdown section
    st.markdown("""
    This bar chart highlights the top 20 most popular CitiBike stations in New York during 2022 based on the number of trips. 

    - The **station names** are displayed along the x-axis.
    - The **number of trips** for each station is represented by the height of the bars.
    - A **color gradient** is applied to the bars, where darker shades represent higher trip counts.

    The chart allows us to identify key stations with the highest demand for CitiBikes. 

    ### Key Insights:
    - The most popular stations include **W 21 St & 6 Ave**, **West St & Chambers St**, and **Broadway & W 58 St**, all exceeding 1,000 trips.
    - High-ranking stations are primarily located in **busy business districts, near transit hubs, and tourist hotspots**.
    - These stations may require additional bikes or docking spaces to meet demand and avoid congestion.
    - Understanding the demand at these locations helps optimize bike distribution and improve service availability at key hotspots.
    """)

    # Create the bar chart
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

###### Interactive map with aggregated bike trips ######

if page == "Interactive map with aggregated bike trips":
    st.markdown("### 🗺️ Most Common CitiBike Trips in New York (2022)")

    # Add interpretation Markdown section
    st.markdown("""
    This map visualizes the most common CitiBike trips in New York during 2022. Each line on the map represents a trip taken between two stations, with the intensity of the lines corresponding to the volume of trips.
    
    - The **thicker lines** indicate higher trip frequencies, showing popular routes between stations.
    - The **map’s color gradient** can help identify high-demand areas where trips are more concentrated.
    - By analyzing the map, we can understand travel patterns and popular routes, which can inform bike distribution strategies.
    
    ### Key Observations:
    - **Central Park S & 6 Ave** is the busiest location, with multiple trips starting and ending at the same spot, all with a trip count of 135.
    - **Roosevelt Island Tramway**, **Soissons Landing**, and **5 Ave & E 72 St** are other frequently used stations with high trip counts (85, 76, and 69, respectively).
    - These locations are popular **tourist spots**:
        - **Central Park S & 6 Ave**: A major entry point to Central Park, near famous landmarks like The Plaza Hotel and 5th Avenue shopping.
        - **Roosevelt Island Tramway**: A well-known tourist attraction offering scenic views of Manhattan.
        - **Soissons Landing**: Located on Governors Island, a seasonal recreational area.
        - **5 Ave & E 72 St**: Near Bethesda Terrace, a famous spot in Central Park.
    
    The most common trips seem to be either within **recreational areas** or near **transit hubs**, suggesting a high demand for short, leisurely rides rather than long-distance commuting.
    """)

    ############################# Add the map ##############################
    path_to_html = "Updated_New_York_Citibike_Trips_Aggregated.html"

    # Read the HTML file with UTF-8 encoding
    with open(path_to_html, 'r', encoding='utf-8') as f: 
        html_data = f.read()

    # Display the map with scrolling and defined width
    st.header("Most Common Citibike Trips in New York")
    components.html(html_data, height=800, width=1200, scrolling=True)


###### Boxplot for User Type ######

if page == "Boxplot for User Type":
    st.markdown("### 📊 Distribution of Trips per Day by User Type (2022)")

    # Add interpretation Markdown section
    st.markdown("""
    This box plot illustrates the distribution of daily trips taken by CitiBike users, categorized by **user type** (Members vs Casual Riders) in 2022. 
    - **Members**: Subscribers who use CitiBike regularly.
    - **Casual Riders**: One-time or occasional users who rent bikes without a membership.

    **Key Observations**:
    - **Median trip counts** for both members and casual riders are slightly above 1000 trips per day.
    - **Members** show a **wider interquartile range (IQR)**, indicating greater variability in daily trips. This suggests that some members use CitiBike frequently while others have more sporadic usage.
    - **Casual riders** have a **narrower IQR**, but the **lower-end outliers** suggest that some casual users occasionally take significantly fewer trips. These users may have irregular trip patterns, possibly linked to weather or seasonal trends.
    - The **whiskers for members** extend further than for casual riders, indicating that member trip counts fluctuate more widely. This could suggest that members, with frequent and varied use, may contribute to the supply-demand imbalance at specific stations.

    **Implication**: The box plot helps us understand the variability in trips by user type, highlighting that the **wide fluctuations in member trips** could contribute to the **cycling supply problem**, particularly during peak demand periods.
    """)

    # Filter data for members and casual riders
    df_member = df_1[df_1['user_type'] == 'member']['trips_per_day']
    df_casual = df_1[df_1['user_type'] == 'casual']['trips_per_day']

    # Create the box plot
    fig, ax = plt.subplots(figsize=(12, 7))

    # Boxplot with custom colors
    box = ax.boxplot([df_member, df_casual], labels=['Member', 'Casual'], patch_artist=True,
                     boxprops=dict(color='black'),  # Border color for boxes
                     whiskerprops=dict(color='black'),
                     flierprops=dict(markerfacecolor='red', marker='o', markersize=8),  # Red for outliers
                     medianprops=dict(color='yellow'))  # Yellow for the median line

    # Apply colors: Blue for Members, Light Purple (#D8BFD8) for Casual Riders
    colors = ['blue', '#D8BFD8']  # Hex code for light purple (thistle)
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)

    # Add titles and labels
    ax.set_title("Distribution of Trips per Day by User Type", fontsize=16)
    ax.set_xlabel("User Type", fontsize=14)
    ax.set_ylabel("Trips per Day", fontsize=14)

    # Display the plot in Streamlit
    st.pyplot(fig)


###### Recommendations ######

if page == "Recommendations":
    st.markdown("### ✅ Recommendations and Strategic Insights for Citi Bike (2022)")

    st.markdown("""
    Based on the comprehensive analysis of Citi Bike trips in **2022**, we’ve identified key operational patterns and supply-demand challenges. The following recommendations are designed to enhance **bike availability**, improve **logistics efficiency**, and support **strategic expansion** efforts:

    ### 🚲 **1. Optimize Bike Redistribution Strategies**
    - **Dynamic Rebalancing:** Implement real-time bike redistribution using predictive algorithms based on historical demand patterns and weather forecasts.
    - **Peak Hour Focus:** Allocate more resources for bike redistribution during **morning and evening peak hours**, especially at high-traffic stations like **Central Park S & 6 Ave** and **Roosevelt Island Tramway**.

    ### 📍 **2. Expand Docking Stations Strategically**
    - **High-Demand Areas:** Add more docking stations near tourist hotspots (e.g., **5 Ave & E 72 St**, **Soissons Landing**) and major transit hubs to reduce overcrowding.
    - **Seasonal Adjustment:** Temporary expansion of docks in recreational areas during **summer months**, aligning with increased casual rider activity.

    ### 🌦️ **3. Weather-Responsive Operations**
    - **Flexible Supply Planning:** Adjust bike supply dynamically based on weather conditions, as ridership trends show a clear correlation with **temperature changes**.
    - **Rainy Day Promotions:** Introduce incentives for casual riders on days with lower demand to balance supply.

    ### 📊 **4. Membership-Focused Campaigns**
    - **Targeted Member Growth:** Since **members contribute to wider fluctuations in trip patterns**, targeted marketing can help smooth out demand variability.
    - **Retention Initiatives:** Incentivize members to use less crowded stations with loyalty rewards.

    ### 📈 **5. Data-Driven Decision Making**
    - **Real-Time Dashboard:** Equip the operations team with a real-time dashboard to monitor bike availability, station status, and demand trends.
    - **Continuous Monitoring:** Regularly update predictive models with fresh data to improve forecasting accuracy.

    ---

    **Final Insight:**  
    The key to solving Citi Bike’s supply challenges lies in leveraging **data-driven insights** to predict demand accurately and implement **agile redistribution strategies**. A proactive approach to managing peak demand, weather impacts, and user behaviour can significantly enhance the user experience across New York City.

    """)

    # Add a closing image or infographic
    from PIL import Image
    img = Image.open("Citi_Bike_Strategy.jpg")  # https://citibikenyc.com/pricing
    st.image(img, caption="Citi Bike's Path to an Optimized Future", use_container_width=True)