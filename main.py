import time
import random
from datetime import datetime

from python_simulation.gps_simulator import GPSSimulator
from python_simulation.vehicle_controller import VehicleController
from python_simulation.geofence import check_geofence
from python_simulation.theft_detector import TheftDetector
from python_simulation.alert_manager import AlertManager
from python_simulation.logger import (
    initialize_log,
    log_vehicle_data
)

# ===================================
# VEHICLE CLASS
# ===================================

class SmartVehicle:

    def __init__(self, vehicle_id):

        self.vehicle_id = vehicle_id

        self.gps = GPSSimulator()

        self.controller = VehicleController()

        self.theft_detector = TheftDetector()

        self.route_history = []

        self.total_distance = 0

        self.last_lat = None

        self.last_lon = None

    def calculate_distance(
            self,
            lat1,
            lon1,
            lat2,
            lon2):

        return (
            ((lat2-lat1)**2)
            +
            ((lon2-lon1)**2)
        ) ** 0.5

    def update(self):

        location = self.gps.move()

        fuel = self.controller.consume_fuel()

        inside_zone = check_geofence(
            location["latitude"],
            location["longitude"]
        )

        security = self.theft_detector.detect(
            inside_zone,
            self.controller.locked,
            location["speed"]
        )

        # route tracking

        if self.last_lat is not None:

            dist = self.calculate_distance(
                self.last_lat,
                self.last_lon,
                location["latitude"],
                location["longitude"]
            )

            self.total_distance += dist

        self.last_lat = location["latitude"]
        self.last_lon = location["longitude"]

        self.route_history.append(
            (
                location["latitude"],
                location["longitude"]
            )
        )

        return {

            "vehicle_id":
            self.vehicle_id,

            "latitude":
            location["latitude"],

            "longitude":
            location["longitude"],

            "speed":
            location["speed"],

            "fuel":
            fuel,

            "engine":
            self.controller.engine,

            "locked":
            self.controller.locked,

            "inside_zone":
            inside_zone,

            "status":
            security["status"],

            "alert":
            security["alert"],

            "distance":
            round(
                self.total_distance,
                4
            )
        }

# ===================================
# ALERT SYSTEM
# ===================================

alert_manager = AlertManager()

# ===================================
# CSV FILE INIT
# ===================================

initialize_log()

# ===================================
# MULTI VEHICLE CREATION
# ===================================

vehicles = [

    SmartVehicle("VH001"),
    SmartVehicle("VH002"),
    SmartVehicle("VH003")

]

# ===================================
# CONTROL FUNCTIONS
# ===================================

def random_actions(vehicle):

    chance = random.randint(1,100)

    if chance < 5:

        vehicle.controller.lock_vehicle()

        print(
            f"{vehicle.vehicle_id} LOCKED"
        )

    elif chance < 10:

        vehicle.controller.unlock_vehicle()

        print(
            f"{vehicle.vehicle_id} UNLOCKED"
        )

    elif chance < 15:

        vehicle.controller.toggle_engine()

        print(
            f"{vehicle.vehicle_id} ENGINE TOGGLED"
        )

# ===================================
# MAIN LOOP
# ===================================

print("\n")
print("="*60)
print(" IoT Vehicle Tracking System Started ")
print("="*60)

while True:

    for vehicle in vehicles:

        random_actions(vehicle)

        data = vehicle.update()

        if data["status"] == "THEFT":

            alert_manager.create_alert(

                "THEFT",

                f"{data['vehicle_id']} : "
                f"{data['alert']}"
            )

        log_vehicle_data(

            data["latitude"],

            data["longitude"],

            data["speed"],

            data["fuel"],

            data["engine"],

            data["locked"],

            data["status"],

            data["alert"]
        )

        print("\n")

        print(
            f"Vehicle : "
            f"{data['vehicle_id']}"
        )

        print(
            f"Time : "
            f"{datetime.now()}"
        )

        print(
            f"Latitude : "
            f"{data['latitude']}"
        )

        print(
            f"Longitude : "
            f"{data['longitude']}"
        )

        print(
            f"Speed : "
            f"{data['speed']} km/h"
        )

        print(
            f"Fuel : "
            f"{data['fuel']} L"
        )

        print(
            f"Engine : "
            f"{data['engine']}"
        )

        print(
            f"Locked : "
            f"{data['locked']}"
        )

        print(
            f"Distance : "
            f"{data['distance']}"
        )

        print(
            f"Status : "
            f"{data['status']}"
        )

        print(
            f"Alert : "
            f"{data['alert']}"
        )

        print("-"*60)

    time.sleep(3)