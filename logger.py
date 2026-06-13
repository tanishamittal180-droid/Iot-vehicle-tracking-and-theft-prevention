import csv
import os
from datetime import datetime

FILE_PATH = "data/vehicle_log.csv"

def initialize_log():

    if not os.path.exists(FILE_PATH):

        with open(
            FILE_PATH,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Timestamp",
                "Latitude",
                "Longitude",
                "Speed",
                "Fuel",
                "Engine",
                "Locked",
                "Status",
                "Alert"
            ])

def log_vehicle_data(
        latitude,
        longitude,
        speed,
        fuel,
        engine,
        locked,
        status,
        alert):

    with open(
        FILE_PATH,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([

            datetime.now(),

            latitude,

            longitude,

            speed,

            fuel,

            engine,

            locked,

            status,

            alert
        ])