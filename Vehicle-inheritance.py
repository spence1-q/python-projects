# i. Create a parent class named Vehicle
class Vehicle:
    def __init__(self, registration_number, model):
        self.registration_number = registration_number
        self.model = model

    # ii. Include a method named displayVehicle()
    def displayVehicle(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Model: {self.model}")


# iii. & iv. Create a child class named Bus that inherits from Vehicle and adds passenger capacity
class Bus(Vehicle):
    def __init__(self, registration_number, model, passenger_capacity):
        super().__init__(registration_number, model)
        self.passenger_capacity = passenger_capacity

    # v. Include a method named displayBus() to display all vehicle information
    def displayBus(self):
        super().displayVehicle()
        print(f"Passenger Capacity: {self.passenger_capacity} seats")


# vi. Create a Bus object and display its details
if __name__ == "__main__":
    my_bus = Bus(registration_number="KCF 123A", model="Howo Kamulu Express", passenger_capacity=33)
    
    print("--- Bus Details ---")
    my_bus.displayBus()
