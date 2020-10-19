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
        return len(orders)

    # ADD ORDER
    # Parameters: Order
    def add_order(self, order):
        orders.append(order)
        total_days_past_PO += order.days_past_PO


v = Vendor('Wills Steel')
print(v)