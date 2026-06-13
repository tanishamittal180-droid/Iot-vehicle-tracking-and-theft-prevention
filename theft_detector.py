class TheftDetector:
    
    def __init__(self):

        self.previous_status = "SAFE"

    def detect(
            self,
            inside_geofence,
            vehicle_locked,
            speed):

        if vehicle_locked and speed > 5:

            return {
                "status": "THEFT",
                "alert": "Locked Vehicle Moving"
            }

        if not inside_geofence:

            return {
                "status": "THEFT",
                "alert": "Vehicle Left Safe Zone"
            }

        return {
            "status": "SAFE",
            "alert": "No Threat"
        }