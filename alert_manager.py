from datetime import datetime

class AlertManager:

    def __init__(self):

        self.alerts = []

    def create_alert(
            self,
            alert_type,
            message):

        alert = {

            "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "type":
            alert_type,

            "message":
            message
        }

        self.alerts.append(alert)

        print(
            f"\n🚨 ALERT: {message}"
        )

        return alert

    def get_alerts(self):

        return self.alerts

    def total_alerts(self):

        return len(self.alerts)