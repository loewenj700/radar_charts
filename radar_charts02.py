import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import streamlit as st

# Load datasets
data_2021 = pd.read_csv('2021_global_crime.csv')
data_2023 = pd.read_csv('2023_global_crime.csv')

# Function to plot radar chart
def plot_radar_chart(data, countries, categories):
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Calculate angles for categories
    angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
    angles += angles[:1]

    for country in countries:
        values = data[data['Country'] == country][categories].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=country)
        ax.fill(angles, values, alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    st.pyplot(fig)

# Streamlit Interface - 2021 Page
def page_2021():
    st.title("Criminal Market Analysis - 2021")
    data = data_2021

    # Country selection
    countries = st.multiselect("Select Countries", options=data['Country'].unique().tolist())
    categories = ["Human trafficking", "Arms trafficking", "Heroin trade", "Cannabis trade"]

    if not countries:
        st.write("Select at least one country.")
    else:
        plot_radar_chart(data, countries, categories)

# Streamlit Interface - 2023 Page
def page_2023():
    st.title("Criminal Market Analysis - 2023")
    data = data_2023

    # Country selection
    countries = st.multiselect("Select Countries", options=data['Country'].unique().tolist())
    categories = ["Human trafficking", "Arms trafficking", "Heroin trade", "Cannabis trade"]

    if not countries:
        st.write("Select at least one country.")
    else:
        plot_radar_chart(data, countries, categories)

# Streamlit Interface - Comparison Page
def page_comparison():
    st.title("Compare 2021 and 2023")

    # Country selection
    countries = st.multiselect("Select Countries", options=data_2021['Country'].unique().tolist())
    categories = ["Human trafficking", "Arms trafficking", "Heroin trade", "Cannabis trade"]

    if not countries:
        st.write("Select at least one country.")
    else:
        st.write("2021 Data")
        plot_radar_chart(data_2021, countries, categories)

        st.write("2023 Data")
        plot_radar_chart(data_2023, countries, categories)

# Page Navigation
page = st.sidebar.selectbox("Select Page", ["2021 Analysis", "2023 Analysis", "Comparison"])
if page == "2021 Analysis":
    page_2021()
elif page == "2023 Analysis":
    page_2023()
else:
    page_comparison()
