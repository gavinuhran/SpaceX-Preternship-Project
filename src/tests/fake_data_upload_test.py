import sys
import os
import operator

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, 'include'))

import init_data
import dictionary_functions

file_location = './data/FakeData.csv'

def rank_vendors(w1, w2, w3, w4):
    weights = [w1, w2, w3, w4]
    vendors = init_data.import_data(file_location, weights)

    sortedVendors = dictionary_functions.sort_descending(vendors)
    normalizing_value = dictionary_functions.get_max_score(sortedVendors)

    for vendor in sortedVendors:
        print(vendor, "{:.5f}".format(sortedVendors[vendor].get_score() / normalizing_value))

rank_vendors(1, 1, 4, 1)
