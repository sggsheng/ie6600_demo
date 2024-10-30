import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#st.title('Class Demo for streamlit')

#st.write('hello world')

penguin = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv')

#st.scatter_chart(data = penguin, x = 'flipper_length_mm', y = 'body_mass_g', x_label = 'Flipper length', y_label = 'Body mass', color = 'species')

#st.bar_chart(data = penguin, x = 'sex', y = 'body_mass_g', x_label = 'Sex', y_label = 'Body mass')

#st.line_chart(data = penguin, x = 'flipper_length_mm', y = 'culmen_depth_mm', x_label = 'Flipper length', y_label = 'Culmen depth', color = 'species')

# Sidebar for user input
st.sidebar.header("Select Options")
selected_category = st.sidebar.selectbox("Select Species", options=['All', 'Adelie', 'Gentoo', 'Chinstrap' ])

if selected_category != 'All':
    filtered_data = penguin[penguin['species'] == selected_category];
else:
    filtered_data = penguin;

st.write('Histogram')
fig, ax = plt.subplots()
ax.hist(filtered_data['culmen_length_mm'], bins=30, color="skyblue", edgecolor="black")
ax.set_title("Matplotlib Histogram for Culmen Lengths")
ax.set_xlabel ("Value")
ax.set_ylabel ("Frequency")

st.pyplot(fig)

st.write("#### Seaborn Density FiLdt")
fig, ax = plt.subplots()
fig = sns.displot(filtered_data['culmen_depth_mm'], color="black", kind='kde', ax=ax, fill=True)
ax.set_title("Seaborn Desity Plot for Culmen Depths")
ax.set_xlabel ("Value")
ax.set_ylabel ("Density")

# Altair scatter plot
st.write("### Altair Scatter Plot")

scatter_plot  = alt. Chart(filtered_data).mark_circle().encode(
    x=alt.X('flipper_length_mm', title='Flipper Length'),
    y=alt.Y('body_mass_g', title='Body Mass'), colorzalt. Color('island', scale=alt. Scale(scheme='tableau10')),
    tooltip=['island', 'flipper_length_mm', 'body_mass_g']
).properties(
    width=600, height=400,
    title="Scatter Plot of Penguins Data"
).interactive() # Allows zooming and panning

             # Display the chart
st.altair_chart(scatter_plot, use_container_width=True)