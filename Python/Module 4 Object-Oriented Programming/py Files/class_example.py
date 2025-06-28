
class Car:
    """
    A simple class representing a car.
    """

    # Class attribute
    wheels = 4

    # Instance attributes (defined in the constructor)
    def __init__(self, make, model, year, color):
        """
        Initializes a new Car object.

        Args:
            make (str): The make of the car (e.g., "Toyota").
            model (str): The model of the car (e.g., "Camry").
            year (int): The manufacturing year of the car.
            color (str): The color of the car.
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False  # Initial state: car is not running

    # Instance methods
    def start_engine(self):
        """
        Starts the car's engine.
        """
        if not self.is_running:
            print(f"Starting the {self.year} {self.make} {self.model}...")
            self.is_running = True
            print("Engine is now running.")
        else:
            print("Engine is already running.")

    def stop_engine(self):
        """
        Stops the car's engine.
        """
        if self.is_running:
            print(f"Stopping the {self.year} {self.make} {self.model}...")
            self.is_running = False
            print("Engine is now stopped.")
        else:
            print("Engine is already stopped.")

    def honk(self):
        """
        Honks the car's horn.
        """
        print("Beep beep!")

    def get_description(self):
        """
        Returns a string describing the car.
        """
        return f"{self.color} {self.year} {self.make} {self.model}"


# Example Usage:
# Creating Car objects
car1 = Car("Toyota", "Camry", 2022, "Silver")
car2 = Car("Honda", "Civic", 2023, "Blue")

# Accessing attributes
print(f"Car 1 is a {car1.get_description()}")  # Output: Car 1 is a Silver 2022 Toyota Camry
print(f"Car 2 has {Car.wheels} wheels")  # Accessing class attribute

# Calling methods
car1.start_engine()  # Output: Starting the 2022 Toyota Camry... Engine is now running.
car1.honk()  # Output: Beep beep!
car1.stop_engine()  # Output: Stopping the 2022 Toyota Camry... Engine is now stopped.
car2.start_engine()
car2.stop_engine()

