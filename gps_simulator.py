import random
import math

class GPSSimulator:

    def __init__(self):

        self.latitude = 31.3260
        self.longitude = 75.5762

        self.speed = 0

    def move(self):

        angle = random.uniform(0,360)

        distance = random.uniform(
            0.0001,
            0.001
        )

        self.latitude += (
            math.cos(math.radians(angle))
            * distance
        )

        self.longitude += (
            math.sin(math.radians(angle))
            * distance
        )

        self.speed = random.randint(
            10,
            80
        )

        return {
            "latitude": round(
                self.latitude,
                6
            ),
            "longitude": round(
                self.longitude,
                6
            ),
            "speed": self.speed
        }