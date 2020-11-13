import csv
from Vendor import *
from xlsx_to_csv import *
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def import_data(file_name, weights):

    vendors = {}
    with open(os.path.join(DATA_DIR, file_name + '.csv'), 'r', encoding='utf-8-sig') as data:
        data_reader = csv.reader(data)
        for row in data_reader:
            # Converts data to proper data types (ints and float for numeric data)
            vendor_name = row[0]
            order_data = [int(i) for i in row[1:-1]] + [int(float(row[-1][:-1])/100)]
            
            # Add vendor to dictionary if not already present
            if vendor_name not in vendors:
                vendor = Vendor(vendor_name)
                vendors[vendor_name] = vendor

            # Add order to vendor's order array
            vendors[vendor_name].add_order(order_data, weights)

    
    # print(vendors['A'])

    return vendors

'''
if __name__ == '__main__':
    main()
'''
