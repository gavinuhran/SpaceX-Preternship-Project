from Order import *

class Vendor:
    name = ''
    score = 0

    orders = []

    total_days_past_PO = 0
    total_lot_size = 0
    total_nonconforming_units = 0
    total_units_downstream_failure = 0
    total_cost_away_from_target = 0

    # CONSTRUCTOR
    # Parameters: string
    def __init__(self, name): 
        self.name = name

    # TO STRING
    # Parameters: 
    def __str__(self):
        return self.name

    # GET NUM ORDERS
    # Parameters: 
    def get_num_orders(self):
        return len(self.orders)

    # ADD ORDER
    # Parameters: Order
    def add_order(self, order):
        self.orders.append(order)

        self.total_days_past_PO += order.days_past_PO
        self.total_lot_size += order.lot_size
        self.total_nonconforming_units += order.nonconforming_units
        self.total_units_downstream_failure += order.units_downstream_failure
        self.total_cost_away_from_target += order.cost_away_from_target

    # GET AVERAGE DAYS PAST PO
    # Parameters: 
    def get_avg_days_past_PO(self):
        return self.total_days_past_PO / float(len(self.orders))

    # GET AVERAGE LOT SIZE
    # Parameters: 
    def get_avg_lot_size(self):
        return self.total_lot_size / float(len(self.orders))

    # GET AVERAGE NONCONFORMING UNITS
    # Parameters: 
    def get_avg_nonconforming_units(self):
        return self.total_nonconforming_units / float(len(self.orders))

    # GET AVERAGE UNITS DOWNSTREAM FAILURE
    # Parameters: 
    def get_avg_units_downstream_failure(self):
        return self.total_units_downstream_failure / float(len(self.orders))

    # GET AVERAGE COST AWAY FROM TARGET
    # Parameters: 
    def get_avg_cost_away_from_target(self):
        return self.total_cost_away_from_target / float(len(self.orders))