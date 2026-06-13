import random

class VehicleController:

    def __init__(self):

        self.engine = True
        self.locked = False

        self.fuel = 50

    def toggle_engine(self):

        self.engine = not self.engine

        return self.engine

    def lock_vehicle(self):

        self.locked = True

    def unlock_vehicle(self):

        self.locked = False

    def consume_fuel(self):

        if self.engine:

            self.fuel -= random.uniform(
                0.05,
                0.3
            )

            if self.fuel < 0:
                self.fuel = 0

        return round(
            self.fuel,
            2
        )

    def vehicle_status(self):

        return {
            "engine": self.engine,
            "locked": self.locked,
            "fuel": round(
                self.fuel,
                2
            )
        }