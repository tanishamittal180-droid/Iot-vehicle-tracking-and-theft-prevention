class CloudSimulator:
    
    def __init__(self):

        self.database = []

    def upload(self, data):

        self.database.append(data)

        print(
            f"☁️ Uploaded : "
            f"{data['vehicle_id']}"
        )

    def get_data(self):

        return self.database