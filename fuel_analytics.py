class FuelAnalytics:
    
    def __init__(self):

        self.history = []

    def update(self, fuel):

        self.history.append(fuel)

    def average_fuel(self):

        if len(self.history) == 0:

            return 0

        return round(
            sum(self.history)
            /
            len(self.history),
            2
        )

    def fuel_consumed(self):

        if len(self.history) < 2:

            return 0

        return round(
            self.history[0]
            -
            self.history[-1],
            2
        )