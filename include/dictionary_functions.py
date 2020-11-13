import operator

def get_max_score_from_unsorted(dictionary):
    vendors = list(dictionary.values())
    max_score = vendors[0].get_score()
    for i in range(1, len(vendors)):
        score = vendors[i].get_score()
        if score > max_score:
            max_score = score
    return max_score


def get_max_score_from_descending(descending_dictionary):
    max = None
    for key in descending_dictionary:
        max = descending_dictionary[key].get_score()
        break
    return max

def convert_tuples_to_dict(tuples):
    new_dict = {}

    for t in tuples:
        new_dict[t[0]] = t[1]

    return new_dict

def sort_ascending(dictionary):
    ascending_tuples = sorted(dictionary.items(), key=operator.itemgetter(1))
    return convert_tuples_to_dict(ascending_tuples)

def sort_descending(dictionary):
    descending_tuples = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return convert_tuples_to_dict(descending_tuples)

def get_all_scores(dictionary):
    max_score = get_max_score_from_unsorted(dictionary)
    sorted_dictionary = sort_ascending(dictionary)
    scores = [dictionary[i].get_score() / max_score for i in sorted_dictionary.keys()]

    return sorted_dictionary.keys(), scores

def get_average_PO(dictionary, vendor):
    v = dictionary[vendor]
    val = float(v.get_avg_days_past_PO)
    return val

def get_avg_costDif(dictionary, vendor):
    v = dictionary[vendor]
    val = float(v.get_avg_cost_away_from_target)
    return val

def get_new_vendor_positions(vendors):
    vendor_positions = {}
    for i in range(len(vendors)):
        vendor_positions[vendors[i]] = i
    return vendor_positions

def get_num_orders(dictionary, vendors):
    num_orders = []
    for vendor in vendors:
        num_orders.append(dictionary[vendor].get_num_orders())
    return num_orders

# Generates a hex color for a string based on a hash
def color_hash(s):
    l = s.lower()
    # Initial large hexadecimal value as initial hash
    h = int('cbf29ce484222325', 16)

    # Run operations to generate unique value for all strings
    for i in range(len(l)):
        b = ord(l[i])
        m = int('1099511628211', 16) 
        h *= m + b
        h ^= b
        h &= 2**32 - 1
    
    # Assign last 3 bytes to red, green, and blue
    r = (h & int('FF0000', 16)) >> 16
    g = (h & int('00FF00', 16)) >> 8
    b = h & int('0000FF', 16)

    # Concatenate hex values of bytes to get hex color code
    return '#' + (hex(r)[2:] + hex(g)[2:] + hex(b)[2:]).zfill(6)
