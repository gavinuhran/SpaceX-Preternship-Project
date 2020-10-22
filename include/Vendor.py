from Order import *

class Vendor:

    # CONSTRUCTOR
    # Parameters: string
    def __init__(self, name): 
        self.name = name
        self.orders = []

        self.total_days_past_PO = 0
        self.total_lot_size = 0
        self.total_nonconforming_units = 0
        self.total_units_downstream_failure = 0
        self.total_cost_away_from_target = 0

        self.total_orders_score = 0

    # TO STRING
    # Parameters: 
    def __str__(self):
        return self.name + ' - Number of orders: ' + str(self.get_num_orders())

    # GET SCORE
    # Parameters: 
    def get_score(self):
        return self.score

    # GET NUM ORDERS
    # Parameters: 
    def get_num_orders(self):
        return len(self.orders)

    # ADD ORDER
    # Parameters: List representation of order data
    def add_order(self, order):
        # Creates new order based on a list of order data
        new_order = Order(self.get_num_orders(), order[0],
                              order[1], order[2], order[3], order[4])
        self.orders.append(new_order)

        self.total_days_past_PO += new_order.days_past_PO
        self.total_lot_size += new_order.lot_size
        self.total_nonconforming_units += new_order.nonconforming_units
        self.total_units_downstream_failure += new_order.units_downstream_failure
        self.total_cost_away_from_target += new_order.cost_away_from_target

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

	# GET THE TOTAL FAILURES FROM THE TOTAL ORDERS
	# Parameters: None
    def get_total_avg_failure(self):
        failures = self.get_avg_days_past_PO() + self.get_avg_nonconforming units() + self.get_avg_units_downstream_failure() + self.get_avg_cost_away_from_target()
		return failures
