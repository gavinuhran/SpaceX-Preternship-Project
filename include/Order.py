class Order:
    def __init__(self, numIn, dIn, lIn, nIn, uIn, cIn):
        self.order_number = numIn
        self.days_past_PO = dIn
        self.lot_size = lIn
        self.nonconforming_units = nIn
        self.units_downstream_failure = uIn
        self.cost_away_from_target = cIn

    def __str__(self):
        return ('ORDER ' + str(self.order_number) + '\n'
                'Days past PO:  ' + str(self.days_past_PO) + '\n'
                'Lot size:  ' + str(self.lot_size) + '\n'
                'Nonconforming units:  ' + str(self.nonconforming_units) + '\n'
                'Units resulting in downstream failure:  ' + str(self.units_downstream_failure) + '\n'
                'Cost away from target (%):  ' + str(self.cost_away_from_target))
