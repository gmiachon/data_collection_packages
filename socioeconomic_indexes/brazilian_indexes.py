"""
This file includes functions for data collection from Brazilian sources
As of now, supported sources are:
  Brazilian Central Bank
"""

import pandas as pd
import datetime

def brazilian_central_bank(table_code, start_date, end_date):
  """
  A code is required to access each index. You can find all the indexes released by Brazilian Central Bank and their codes at:
  https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries
  """
  
  # Getting data from url
  url = f"http://api.bcb.gov.br/dados/serie/bcdata.sgs.{table_code}/dados?formato=json"
  df = pd.read_json(url)
  df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  
  # Filtering for the relevant dates
  conv_start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d")
  conv_end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
  return df[(df['data'] >= conv_start_date) & (df['data'] <= conv_end_date)].sort_values(by=['data'])
