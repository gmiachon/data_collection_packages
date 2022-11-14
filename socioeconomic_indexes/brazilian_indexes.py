"""
This file includes functions for data collection from Brazilian sources
As of now, supported sources are:
  Brazilian Central Bank
"""

import pandas as pd
import datetime
import warnings

def brazilian_central_bank(table_code: int, start_date: str, end_date: str) -> pd.core.frame.DataFrame:
    """
    A code is required to access each index. You can find all the indexes released by Brazilian Central Bank and their codes at:
    https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries
    
    start_date and end_date must be passed as strings in format '%Y-%m-%d'
    """
  
    # Check if function receives the correct parameter types
    if type(table_code) not in [int, str]:
        raise TypeError("table_code must be either a integer or a string")

    if type(start_date) != str or type(end_date) != str:
        raise TypeError("date parameters must be strings")

    # Check if function receives the correct parameter values
    try:
        bool(datetime.datetime.strptime(start_date, '%Y-%m-%d'))
        bool(datetime.datetime.strptime(end_date, '%Y-%m-%d'))
    except ValueError:
        raise ValueError("Data must be in format '%Y-%m-%d'")

    if int(table_code) <= 0:
        raise ValueError("table_code value must be greater than zero")

    # Getting data from url
    url = f"http://api.bcb.gov.br/dados/serie/bcdata.sgs.{table_code}/dados?formato=json"

    # Using try / catch to check for bad requests
    try:
        df = pd.read_json(url)
    except ValueError:
        raise ValueError("Bad request. Check https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries for available indexes and their codes")

    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  
    # Filtering for the relevant dates
    conv_start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d")
    conv_end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")

    # Warnings
    if df.data.iloc[0] > conv_start_date:
        warnings.warn(f"First available entry in table {table_code} is in {df.data.iloc[0]:%Y-%m-%d}, while user specified start date is {start_date}.", category=UserWarning)

    if df.data.iloc[-1] < conv_end_date:
        warnings.warn(f"Last available entry in table {table_code} is in {df.data.iloc[-1]:%Y-%m-%d}, while user specified end date is {end_date}.", category=UserWarning)

    return df[(df['data'] >= conv_start_date) & (df['data'] <= conv_end_date)].sort_values(by=['data'])