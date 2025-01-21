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

    # Calculate angles
    angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
    angles += angles[:1]

    for country in countries:
        values = data[data['Country'] == country][categories].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=country)
        ax.fill(angles, values, alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title("Radar Chart: Criminal Market Breakdown")
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    st.pyplot(fig)


# Streamlit application
st.title("Global Criminal Market Analysis")

# Year selection
year = st.selectbox("Select Year", [2021, 2023])
data = data_2021 if year == 2021 else data_2023

# Country selection
countries = st.multiselect("Select Countries", options=data['Country'].unique().tolist())

# Categories for radar chart
categories = ["Human trafficking", "Arms trafficking", "Heroin trade", "Cannabis trade"]

# Display radar chart or a message if no countries are selected
if not countries:
    st.write("Select at least one country.")
else:
    st.write("Radar Chart: Criminal Market Profile")
    plot_radar_chart(data, countries, categories)

# Additional example: High human trafficking scores
st.write("Countries with High Human Trafficking Scores")
if year == 2021:
    high_trafficking = data_2021[data_2021['Human trafficking'] > 7]['Country'].tolist()
else:
    high_trafficking = data_2023[data_2023['Human trafficking'] > 7]['Country'].tolist()
st.write("Top countries:", high_trafficking)

# Example to compare years
if st.checkbox("Compare 2021 and 2023 Data"):
    st.write("2021 Data")
    plot_radar_chart(data_2021, countries, categories)
    st.write("2023 Data")
    plot_radar_chart(data_2023, countries, categories)
