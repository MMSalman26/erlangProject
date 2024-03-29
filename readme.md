# Erlang B Calculator

This Streamlit app calculates Erlang B traffic model parameters and visualizes the results using dynamic plots.

## Overview

The Erlang B model is commonly used in telecommunications and call center management to estimate the number of trunks (lines) required to handle a given offered traffic (Erlang) while maintaining a specific blocking probability.

## Features

- Input parameters:
  - Offered traffic (Erlang)
  - MINIMUM GRADE OF SERVICE
  - OBJECTIVE GRADE OF SERVICE
  - Maximum number of trunks
- Results displayed in a table format
- Dynamic plots:
  - Offered vs Trunks
  - Carried vs Trunks
  - Cumulative vs Trunks
  - P vs Trunks (blocking probability)

## Usage

1. Install dependencies:

   ```
   pip install streamlit pandas matplotlib
   ```

2. Run the app:

   ```
   streamlit run app.py
   ```

3. Use the sidebar to input parameters and explore the results.

## Data Sources

The app generates synthetic data for demonstration purposes. Replace this with your actual data when using the app in a real-world scenario.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

Feel free to add more sections or customize the README as needed. Happy coding! 🚀👍
