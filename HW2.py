import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

st.write("""
# Describing Iris Dataset
Visualizing the relationship between Petal_length, Sepa_width and Sepal_length
""")

df_iris = sns.load_dataset("iris")

fig = px.scatter_3d(df_iris, x='petal_length', y='sepal_width', z='petal_width',color='species', size = "sepal_length", opacity = 0.7, size_max = 14)
fig = fig.update_layout(margin = dict(l=1, r=0, b=0,t=0))

st.plotly_chart(fig, use_container_width=True)