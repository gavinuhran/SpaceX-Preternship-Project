class Order:

    # CONSTRUCTOR
    # Parameters: int, int, int, int, int, int, float[]
    def __init__(self, numIn, dIn, lIn, nIn, uIn, cIn, weights):
        self.order_number = numIn
        self.days_past_PO = dIn
        self.lot_size = lIn
        self.nonconforming_units = nIn
        self.units_downstream_failure = uIn
        self.cost_away_from_target = cIn

        self.score = self.get_score(weights)

    # GET SCORE
    # Parameters: float[4] -> days_past_PO weight, nonconforming weight, downstream fail weight, cost weight
    def get_score(self, weights):
        # Invert scores to make weighting formula work properly
        weights = [11 - i for i in weights]
        
        return 1 / ((weights[0])*(1+self.days_past_PO))  \
            + 1 / ((weights[1])*(self.nonconforming_units) + (weights[2])*(self.units_downstream_failure)) \
            + 1 / ((weights[3])*(100 + self.cost_away_from_target))
    
    def __str__(self):
        return ('ORDER ' + str(self.order_number) + '\n'
                'Days past PO:  ' + str(self.days_past_PO) + '\n'
                'Lot size:  ' + str(self.lot_size) + '\n'
                'Nonconforming units:  ' + str(self.nonconforming_units) + '\n'
                'Units resulting in downstream failure:  ' + str(self.units_downstream_failure) + '\n'
                'Cost away from target (%):  ' + str(self.cost_away_from_target) + '\n'
                'Score:  ' + str(self.score))
