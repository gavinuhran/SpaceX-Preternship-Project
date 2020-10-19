import csv
from Vendor import *

def main():
    vendors = {}
    with open('./include/data/FakeData.csv', 'r', encoding='utf-8-sig') as data:
        data_reader = csv.reader(data)
        for row in data_reader:
            # Converts data to proper data types (ints and float for numeric data)
            vendor_name = row[0]
            order_data = [int(i) for i in row[1:-1]] + [int(row[-1][:-1])]
            
            # Add vendor to dictionary if not already present
            if vendor_name not in vendors:
                vendor = Vendor(vendor_name)
                vendors[vendor_name] = vendor

            # Add order to vendor's order array
            vendors[vendor_name].add_order(order_data)

    print(vendors['A'])

if __name__ == '__main__':
    main()
