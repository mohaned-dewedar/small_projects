import pandas as pd
import streamlit as st

df = pd.read_csv("D:/Tutorials/small_projects/Langchain/streamlit_with_agent/2019.csv", index_col=0)
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


def rank_countries_by_metric(metric='Overall rank',k=5,ascending=True):
    # Sort the DataFrame based on the metric
    sorted_df = df.sort_values(by=metric, ascending=ascending)
    # st.dataframe(sorted_df.head(k))
    st.table(sorted_df.head(k))


    return "Table shown via streamlit"

