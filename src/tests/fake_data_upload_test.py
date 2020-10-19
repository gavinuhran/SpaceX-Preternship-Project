import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, 'include'))

import init_data

def print_vendor(vendor):
    print('------------------------------------------')
    print(vendor)
    print('Score:  ' + str(vendor.get_score()))
    print('Avg days past PO:  ' + str(vendor.get_avg_days_past_PO()))
    print('Avg lot size:  ' + str(vendor.get_avg_lot_size()))
    print('Avg nonconforming units:  ' + str(vendor.get_avg_nonconforming_units()))
    print('Avg units downstream failure:  ' + str(vendor.get_avg_units_downstream_failure()))
    print('Avg cost away from target (%):  ' + str(vendor.get_avg_cost_away_from_target()))


file_location = './data/FakeData.csv'

vendors = init_data.import_data(file_location)

for vendor in vendors:
    print_vendor(vendors[vendor])