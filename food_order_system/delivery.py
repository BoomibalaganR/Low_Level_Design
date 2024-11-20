class DeliveryDetails:
    def __init__(self, address: str, estimated_time: str):
        self.address = address
        self.estimated_time = estimated_time

    def get_address(self):
        return self.address

    def get_estimated_time(self):
        return self.estimated_time
