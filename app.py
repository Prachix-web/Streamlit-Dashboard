import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
# df = pd.read_csv('path_to_your_file.csv')
df = pd.read_csv('Imports_Exports_Dataset.csv')

# Set up the page layout for the dashboard
st.set_page_config(
    page_title="Imports & Exports Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Imports & Exports Data Dashboard")

# Sidebar for user input
st.sidebar.header("Choose a Visualization")
st.sidebar.markdown("Select from the options below to display specific visualizations:")

# Plot 1: Scatter Plot (Quantity vs Value)
if st.sidebar.checkbox("Scatter Plot: Quantity vs Value", value=True):
    st.subheader("Scatter Plot: Quantity vs Value")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Quantity'], df['Value'], alpha=0.7, color='blue')
    ax.set_title('Scatter Plot between Quantity and Value')
    ax.set_xlabel('Quantity')
    ax.set_ylabel('Value')
    st.pyplot(fig)

# Plot 2: Box Plot (Numerical Variables)
if st.sidebar.checkbox("Box Plot: Numerical Variables", value=True):
    st.subheader("Box Plot: Numerical Variables")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df[['Quantity', 'Value', 'Weight']], ax=ax)
    ax.set_title("Box Plot of Quantity, Value, and Weight")
    st.pyplot(fig)

# Plot 3: Pie Chart (Top 5 Countries by Transactions)
if st.sidebar.checkbox("Pie Chart: Top 5 Countries by Transactions", value=True):
    st.subheader("Pie Chart: Top 5 Countries by Transactions")
    country_data = df['Country'].value_counts().nlargest(5)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(country_data, labels=country_data.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Top 5 Countries by Transactions")
    st.pyplot(fig)

# Plot 4: Correlation Matrix
if st.sidebar.checkbox("Correlation Matrix", value=True):
    st.subheader("Correlation Matrix")
    fig, ax = plt.subplots(figsize=(10, 6))
    corr_matrix = df[['Quantity', 'Value', 'Weight']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
    ax.set_title("Correlation Matrix")
    st.pyplot(fig)

# Customize footer or branding
st.markdown("""
    <style>
    footer {visibility: hidden;}
    .css-1d391kg {padding-top: 1rem;}
    </style>
    Powered by Streamlit
    """, unsafe_allow_html=True)

# Add some spacing
st.markdown("<br><br>", unsafe_allow_html=True)

