"""Module with helper functions for Environment Canada weather data.
"""

# We'll use the requests library to download data from Environment Canada website
import requests

def welcome():
    """Print a silly welcome message."""
    print('Hello! Thank you for importing the ecweather library!')
    return None


def download_daily_raw(env_canada_id, year, savefile='test.csv', verbose=True):
    """Download CSV file of daily data for selected station and year"""
    
    # URL endpoint and query parameters
    url_endpoint = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html'
    params = {'format' : 'csv', 
              'stationID' : env_canada_id,
              'Year' : year,
              'Month' : '01',
              'Day' : '01',
              'timeframe' : '2',
              'submit' : ' Download Data'}

    # Send GET request
    response = requests.get(url_endpoint, params=params)
    
    # Download CSV file
    if verbose:
        print(f'Saving to {savefile}')
    with open(savefile, 'wb') as f:
        f.write(response.content)
    
    return None