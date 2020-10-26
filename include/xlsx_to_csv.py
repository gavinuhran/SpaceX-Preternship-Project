import xlrd
import csv
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def csv_from_excel(sheet_name):
    wb = xlrd.open_workbook(os.path.join(DATA_DIR, sheet_name + '.xlsx'))
    sh = wb.sheet_by_index(0)
    your_csv_file = open('data/' + sheet_name + '.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
