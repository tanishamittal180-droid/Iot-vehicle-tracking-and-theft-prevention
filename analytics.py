import pandas as pd

class AnalyticsEngine:

    def __init__(
            self,
            file_path):

        self.file_path = file_path

    def load_data(self):

        return pd.read_csv(
            self.file_path
        )

    def total_records(self):

        df = self.load_data()

        return len(df)

    def average_speed(self):

        df = self.load_data()

        return round(
            df["Speed"].mean(),
            2
        )

    def max_speed(self):

        df = self.load_data()

        return round(
            df["Speed"].max(),
            2
        )

    def total_alerts(self):

        df = self.load_data()

        alerts = df[
            df["Status"] == "THEFT"
        ]

        return len(alerts)

    def remaining_fuel(self):

        df = self.load_data()

        return round(
            df.iloc[-1]["Fuel"],
            2
        )