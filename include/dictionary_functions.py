import operator

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

def get_max_score(descending_dictionary):
    max = None
    for key in descending_dictionary:
        max = descending_dictionary[key].get_score()
        break
    return max

def get_all_scores(dictionary):
    sorted_dictionary = sort_ascending(dictionary)
    scores = [dictionary[i].get_score() * 100 for i in sorted_dictionary.keys()]

    return sorted_dictionary.keys(), scores
