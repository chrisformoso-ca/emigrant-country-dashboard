# Emigrant Country Dashboard

This project provides an interactive dashboard for analyzing emigrant data from 1981 to 2022 across various countries. The dashboard is built using Streamlit and offers various visualizations and statistics to help understand emigration trends.

## Features

- Total Emigrant Count Over Time with Trendline
- Emigrant Count Over Time by Country
- Cumulative Emigrant Count by Country
- Percentage of Emigrants by Country
- Emigrant Ratio Over Time by Country
- Descriptive Statistics
- Data Download Option

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/emigrant-country-dashboard.git
   cd emigrant-country-dashboard
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have the cleaned data file `Cleaned_Emigrant_Data.xlsx` in the project directory.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Data Cleaning

The raw data is cleaned using the script in `clean_data.ipynb`. This Jupyter notebook processes the original Excel file and creates the `Cleaned_Emigrant_Data.xlsx` file used by the main application.

## File Structure

- `app.py`: Main Streamlit application
- `clean_data.ipynb`: Jupyter notebook for data cleaning
- `Cleaned_Emigrant_Data.xlsx`: Processed data file
- `Emigrant-1981-2022-MajorCountry.xlsx`: Original data file
- `README.md`: This file
- `requirements.txt`: List of Python package dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).