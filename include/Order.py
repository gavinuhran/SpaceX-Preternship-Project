class Order:
    order_number = -1

    days_past_PO = 0
    lot_size = 0
    nonconforming_units = 0
    units_downstream_failure = 0
    cost_away_from_target = 0

    def __init__(self, numIn, dIn, lIn, nIn, uIn, cIn):
        self.order_number = numIn
        self.days_past_PO = dIn
        self.lot_size = lIn
        self.nonconforming_units = nIn
        self.units_downstream_failure = uIn
        self.cost_away_from_target = cIn

    def __str__(self):
        return 'Order ' + str(self.order_number)

o = Order(2, 8, 432, 9, 1, 40)
print(o)