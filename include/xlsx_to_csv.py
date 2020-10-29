import xlrd
import csv
import sys
import os

import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def xlsx_to_csv(sheet_name):
    # Read and store content of an excel file
    read_file = pd.read_excel(os.path.join(DATA_DIR, sheet_name + '.xlsx'))

    # Write the dataframe object into csv file
    read_file.to_csv('data/' + sheet_name + '.csv', index = None, header = False, float_format = '%.2f%%') 
