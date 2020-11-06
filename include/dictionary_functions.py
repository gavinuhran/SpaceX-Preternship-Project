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

def get_total_failure_rate(dictionary, vendor):
    v = dictionary[vendor]
    lot_size = v.total_lot_size
    nonconforming_units = v.total_nonconforming_units
    units_downstream_failure = v.total_units_downstream_failure

    return (nonconforming_units + units_downstream_failure) / lot_size

def get_new_vendor_positions(vendors):
    vendor_positions = {}
    for i in range(len(vendors)):
        vendor_positions[vendors[i]] = i
    return vendor_positions