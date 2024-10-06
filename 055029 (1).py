import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load your dataset (You can use your file or a sample dataset)
# df = pd.read_csv('path_to_your_file.csv')
df = pd.read_csv('Imports_Exports_Dataset.csv')

st.title("Imports & Exports Data Analysis")

# Sidebar for user input
st.sidebar.header("User Input Features")
st.sidebar.markdown("Use the options below to select features for analysis.")

# Display dataset
if st.checkbox("Show Dataset"):
    st.write(df.head())

# Basic Statistics
st.header("Basic Descriptive Statistics")
st.subheader("Central Tendency and Dispersion")

# Numerical columns for analysis
num_cols = ['Quantity', 'Value', 'Weight']

# Central Tendency & Dispersion
if st.checkbox("Show Central Tendency & Dispersion"):
    min_values = df[num_cols].min()
    max_values = df[num_cols].max()
    mean_values = df[num_cols].mean()
    median_values = df[num_cols].median()
    mode_values = df[num_cols].mode().iloc[0]
    std_deviation = df[num_cols].std()
    
    st.write("Minimum Values:", min_values)
    st.write("Maximum Values:", max_values)
    st.write("Mean:", mean_values)
    st.write("Median:", median_values)
    st.write("Mode:", mode_values)
    st.write("Standard Deviation:", std_deviation)

# Visualizations
st.header("Visualizations")

# Scatter Plot
if st.checkbox("Show Scatter Plot"):
    plt.scatter(df['Quantity'], df['Value'], alpha=0.7, color='blue')
    plt.title('Scatter Plot between Quantity and Value')
    plt.xlabel('Quantity')
    plt.ylabel('Value')
    st.pyplot(plt.gcf())  # Use plt.gcf() to get the current figure

# Box Plot
if st.checkbox("Show Box Plot"):
    sns.boxplot(data=df[num_cols])
    plt.title("Box Plot of Quantity, Value, and Weight")
    st.pyplot(plt.gcf())

# Pie Chart
if st.checkbox("Show Pie Chart of Countries"):
    country_data = df['Country'].value_counts().nlargest(5)
    plt.pie(country_data, labels=country_data.index, autopct='%1.1f%%', startangle=90)
    plt.title("Top 5 Countries by Transactions")
    st.pyplot(plt.gcf())

# Advanced Tests
st.header("Statistical Tests")

# t-test between 'Value' and 'Weight'
if st.checkbox("Show t-test"):
    t_stat, t_p_value = stats.ttest_ind(df['Value'], df['Weight'], equal_var=False)
    st.write(f"t-statistic: {t_stat}, p-value: {t_p_value}")

# Polynomial Regression (Degree 2) between 'Quantity' and 'Value'
st.subheader("Polynomial Regression")
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(df[['Quantity']])
y = df['Value']

model = LinearRegression()
model.fit(X_poly, y)

# R-squared value
y_pred = model.predict(X_poly)
r2 = r2_score(y, y_pred)
st.write(f"R-squared value of polynomial regression: {r2}")

if st.checkbox("Show Regression Coefficients"):
    st.write("Coefficients:", model.coef_)
    st.write("Intercept:", model.intercept_)

# Correlation Matrix
st.header("Correlation Matrix")
if st.checkbox("Show Correlation Matrix"):
    corr_matrix = df[num_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix")
    st.pyplot(plt.gcf())

# Footer
st.write("Powered by Streamlit")
