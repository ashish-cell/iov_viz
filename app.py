import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Set the title
st.title("Visualization of Truck behaviors for different risk frequencies")

# Read in your dataset
# Replace 'your_data.csv' with the path to your actual dataset
data = pd.read_csv("data_with_risk_tag.csv")

plot_type = st.selectbox("Select plot type:", ["Violin Plot", "Histogram", "Box Plot"])

# Select the numeric and categorical columns
numeric_column = st.selectbox("Select a numeric variable:", data.select_dtypes(include="number").columns)
categorical_column = st.selectbox("Select a categorical variable:", data.select_dtypes(include="object").columns)

# Select the plot type


# Create the selected plot using Seaborn
fig, ax = plt.subplots()

if plot_type == "Violin Plot":
    sns.violinplot(x=categorical_column, y=numeric_column, data=data, palette="viridis", ax=ax)
    plt.title(f"Distribution of {numeric_column} by {categorical_column}")

elif plot_type == "Histogram":
    sns.histplot(data=data, x=numeric_column, hue=categorical_column, kde=True, ax=ax)
    plt.title(f"Histogram of {numeric_column} by {categorical_column}")

elif plot_type == "Box Plot":
    sns.boxplot(x=categorical_column, y=numeric_column, data=data, palette="viridis", ax=ax)
    plt.title(f"Box Plot of {numeric_column} by {categorical_column}")

# Display the plot in Streamlit
st.pyplot(fig)