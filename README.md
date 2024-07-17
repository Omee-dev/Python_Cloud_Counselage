# Student Data Analysis with Streamlit

## Overview
This project is a data analysis application built using Streamlit. It processes and visualizes student data to answer various queries related to GPA, family income, experience, and other attributes. The application allows users to interactively select and execute queries to gain insights from the dataset.

## Features
- **Load and display dataset**: Load student data from an Excel file and display it in the app.
- **Execute various queries**: Answer specific questions about the data, such as the average GPA, distribution of graduation years, experience with Python, etc.
- **Visualization**: Display data insights using visualizations like bar plots and heatmaps.
- **Dynamic thresholds**: Adjust thresholds for specific queries dynamically using sliders.
- **Show code**: Display the code used to execute the selected query.
- **Reference data**: Option to view the reference dataset within the app.

## Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Omee-dev/Python_Cloud_Counselage.git
   cd cloud-counselage-project
2. Install the required packages:
   ```sh
   pip install -r requirements.txt
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
## File Structure
- app.py: Main application file containing the Streamlit code.
- Input/Data analyst Data.xlsx: Input dataset file.(Download from IAC and then move it to Input folder)
- requirements.txt: List of dependencies required to run the app.
