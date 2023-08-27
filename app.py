import streamlit as st
import pandas as pd
import base64
import numpy as np
import plost   # Data Visualisation
from PIL import Image # to import image 
import seaborn as sns
# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Streamlit Project !!!!!')
st.header('This is a header')
st.markdown('Streamlit is **_really_ cool**.')
st.title("Pharmaceutical-Sales-prediction-across-multiple-stores")
st.write ("welcome")
st.write ("Mani")

# Page Setting

import matplotlib.pyplot as plt  # Corrected import statement for data visualization

train_data=pd.read_csv("train.csv")
sample = pd.read_csv('sample_submission.csv')
test_data=pd.read_csv("test.csv")
store=pd.read_csv("store.csv")

correlation_matrix = train_data[['Promo', 'Customers', 'Sales']].corr()

# Plot the heatmap
st.title('Correlation Heatmap: Promo, Customers, and Sales')

# Display heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
st.pyplot(fig)




import os


# Read the data
sample = pd.read_csv("sample_submission.csv")
store = pd.read_csv('store.csv')
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Display the dataframes
st.subheader("Sample Data:")
st.write(sample)

st.subheader("Store Data:")
st.write(store)

st.subheader("Train Data:")
st.write(train)

st.subheader("Test Data:")
st.write(test)









        