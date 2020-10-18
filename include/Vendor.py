class Vendor:
    name = ''
    score = -1

    orders = []

    avg_days_past_PO = -1
    '''avg_lot_size = -1
    avg_nonconforming_units = -1
    avg_units_downstream_failure = -1
    avg_cost_away_from_target = -1'''


    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

v = Vendor('Wills Steel')
print(v)