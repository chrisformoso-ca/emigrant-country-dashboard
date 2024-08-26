import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the cleaned data
file_path = 'Cleaned_Emigrant_Data.xlsx'
df = pd.read_excel(file_path)

# Data Processing

# Calculate cumulative emigrants per country
cumulative_data = df.groupby('Country')['Emigrant_Count'].sum().reset_index()
cumulative_data = cumulative_data.sort_values(by='Emigrant_Count', ascending=False)

# Calculate total emigrants per year
total_emigrants_per_year = df.groupby('Year')['Emigrant_Count'].sum().reset_index()

# Calculate trendline using linear regression
X = total_emigrants_per_year['Year'].values.reshape(-1, 1)
y = total_emigrants_per_year['Emigrant_Count'].values
model = LinearRegression()
model.fit(X, y)
trendline = model.predict(X)

# Streamlit App Layout

# Main title
st.title('Emigrant Data Analysis (1981-2022)')

# Total Emigrant Count Over Time with Trendline
st.subheader('Total Emigrant Count Over Time with Trendline')
fig_total_line = go.Figure()

# Add the original data line
fig_total_line.add_trace(go.Scatter(
    x=total_emigrants_per_year['Year'], 
    y=total_emigrants_per_year['Emigrant_Count'],
    mode='lines', 
    name='Total Emigrant Count'
))

# Add the trendline
fig_total_line.add_trace(go.Scatter(
    x=total_emigrants_per_year['Year'], 
    y=trendline,
    mode='lines', 
    name='Trendline', 
    line=dict(dash='dash', color='red')
))

fig_total_line.update_layout(
    title='Total Emigrant Count Over Time',
    yaxis_title='Total Emigrant Count', 
    xaxis_title='Year', 
    height=600
)
st.plotly_chart(fig_total_line)

# Emigrant Count Over Time by Country
st.subheader('Emigrant Count Over Time by Country')
fig_line = px.line(
    df, 
    x='Year', 
    y='Emigrant_Count', 
    color='Country', 
    title='Emigrant Count Over Time by Country'
)
fig_line.update_layout(
    legend_title_text='Country', 
    yaxis_title='Emigrant Count', 
    xaxis_title='Year', 
    height=600
)
st.plotly_chart(fig_line)

# Cumulative Emigrant Count by Country
st.subheader('Cumulative Emigrant Count by Country')
fig_bar = px.bar(
    cumulative_data, 
    x='Emigrant_Count', 
    y='Country', 
    orientation='h', 
    title='Cumulative Emigrant Count by Country'
)
fig_bar.update_layout(
    xaxis_title='Emigrant Count', 
    yaxis_title='Country', 
    height=600
)
st.plotly_chart(fig_bar)

# Percentage of Emigrants by Country
st.subheader('Percentage of Emigrants by Country')
fig_pie = px.pie(
    cumulative_data, 
    names='Country', 
    values='Emigrant_Count', 
    title='Percentage of Emigrants by Country'
)
fig_pie.update_traces(textinfo='percent+label')
st.plotly_chart(fig_pie)

# 100% Stacked Line Chart for Emigrant Ratio Over Time
st.subheader('Emigrant Ratio Over Time by Country')
df_grouped = df.groupby(['Year', 'Country'])['Emigrant_Count'].sum().reset_index()
df_pivot = df_grouped.pivot(index='Year', columns='Country', values='Emigrant_Count').fillna(0)
df_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0)

fig_stacked = go.Figure()
for country in df_normalized.columns:
    fig_stacked.add_trace(go.Scatter(
        x=df_normalized.index, 
        y=df_normalized[country], 
        mode='lines', 
        stackgroup='one', 
        name=country
    ))

fig_stacked.update_layout(
    title='Emigrant Ratio Over Time by Country', 
    xaxis_title='Year', 
    yaxis_title='Ratio', 
    height=600
)
st.plotly_chart(fig_stacked)

# Descriptive Statistics
st.subheader('Descriptive Statistics')
statistics = df.groupby('Country').agg(
    Total_Emigrants=('Emigrant_Count', 'sum'),
    Average_Per_Year=('Emigrant_Count', 'mean'),
    Min_Emigrants=('Emigrant_Count', 'min'),
    Max_Emigrants=('Emigrant_Count', 'max')
).reset_index()

statistics = statistics.sort_values(by='Total_Emigrants', ascending=False)
st.write(statistics)

# Download Options
st.subheader('Download Options')
st.download_button(
    label="Download data as CSV",
    data=df.to_csv(index=False),
    file_name='emigrant_data.csv',
    mime='text/csv',
)
