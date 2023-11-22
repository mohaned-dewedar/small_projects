import pandas as pd
import streamlit as st
import plotly.express as px
import pycountry_convert as pc
import os

def load_csv(file_name):
    # Get the current working directory of the script
    directory = os.getcwd()
    # Construct the file path using os.path.join
    file_path = os.path.join(directory, file_name)
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path, index_col=0)
    
    return df
    
df = load_csv("2019.csv")
column_mapping = {
    "Score": "score",
    "GDP per capita": "gdp_per_capita",
    "Social support": "social_support",
    "Healthy life expectancy": "healthy_life_expectancy",
    "Freedom to make life choices": "freedom_to_make_life_choices",
    "Generosity": "generosity",
    "Perceptions of corruption": "perceptions_of_corruption"
}

df.rename(columns=column_mapping, inplace=True)

def country_to_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    except:
        return "Unknown"  # If the country name is not found or conversion fails

# Add a 'continent' column to the DataFrame
df['continent'] = df['Country or region'].apply(country_to_continent)


def rank_countries_by_metric(metric='Overall rank',k=5,ascending=False):
    # Sort the DataFrame based on the metric
    sorted_df = df.sort_values(by=metric, ascending=ascending)
    # st.dataframe(sorted_df.head(k))
    st.table(sorted_df.head(k))


    return "Table is shown "

def plot_scatter(metric_x, metric_y,continent=None):
    global df
    if metric_x not in df.columns or metric_y not in df.columns:
        raise ValueError("One or both of the specified metrics do not exist in the DataFrame.")
    
    if continent:
        df = df[df['continent'] == continent]
    
    
    fig = px.scatter(df, x=metric_x, y=metric_y, hover_name='Country or region',color='continent',
                     title=f'{metric_x} vs {metric_y}' + (f' in {continent}' if continent else '') + ' for each Country',
                     size_max=60, template='simple_white', opacity=0.7)
    fig.update_traces(textposition='top center')
    fig.update_traces(marker=dict(size=10, opacity=0.5),  # Adjust size and opacity here
                      selector=dict(mode='markers+text'))
    fig.update_layout(
        xaxis_title=metric_x,
        yaxis_title=metric_y,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        hovermode='closest',  # Update hover information
    )
    # Enable zoom and pan interaction
    fig.update_layout(dragmode='pan')
    st.plotly_chart(fig, use_container_width=True)
    return "Chart Plotted"

def create_pair_plot(continent=None):
    global df

    if continent:
        df = df[df['continent'] == continent]
    numeric_columns = df.select_dtypes(include=['number']).columns
    numeric_df = df[numeric_columns]
    
    # Create a pair plot of the numeric columns
    fig = px.scatter_matrix(numeric_df,
                            dimensions=numeric_columns,
                            title='Pair Plot of Numeric Metrics')
    fig.update_layout(
    font=dict(size=6)  # Adjust the size as needed to prevent overlap
)
    # Update markers with increased opacity and smaller size
    fig.update_traces(diagonal_visible=False, marker=dict(opacity=0.8, size=5))



    # Customize the layout
    fig.update_layout(
        dragmode='select',
        width=1200,
        height=1200,
    )
    st.plotly_chart(fig, use_container_width=True)
    return "Chart Plotted"


def create_continent_plot(metric,chart_type='box'):
    global df
    # Check if the metric exists
    if metric not in df.columns:
        raise ValueError("The specified metric does not exist in the DataFrame.")

     # Determine the type of plot to create
    if chart_type == 'box':
        fig = px.box(df, x='continent', y=metric, color='continent',
                     title=f'Distribution of {metric} by Continent')
    
    elif chart_type == 'bar':
        # For bar plots, you might want to aggregate the data
        aggregated_data = df.groupby('continent')[metric].mean().reset_index()
        fig = px.bar(aggregated_data, x='continent', y=metric, color='continent',
                     title=f'Average {metric} by Continent')
    elif chart_type == 'histogram':
        # Histograms will show the distribution of the metric across all continents
        fig = px.histogram(df, x=metric, color='continent',
                           title=f'Distribution of {metric} across Continents')
    else:
        raise ValueError("Unsupported chart type. Choose from 'box','bar', or 'histogram'.")
    st.plotly_chart(fig, use_container_width=True)
    return "Box_plot plotted"