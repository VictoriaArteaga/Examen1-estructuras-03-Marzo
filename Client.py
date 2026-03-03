class Client:

    def __init__(self, name: str, phone: str, address: str, clientId: int):
        self.name = name
        self.phone = phone
        self.address = address
        self.clientId = clientId

    def __str__(self):
        return f"{self.name} (ID: {self.clientId})"