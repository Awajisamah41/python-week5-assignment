# This is the base class for all vehicles.
class Vehicle:
    def __init__(self, name):
        self.name = name

    # This is the 'move' method. Each child class will provide its own
    # specific implementation of this method.
    def move(self):
        """A generic method for a vehicle's movement."""
        print(f"{self.name} is moving.")


# The 'Car' class inherits from 'Vehicle'.
class Car(Vehicle):
    # This is the Car's specific implementation of the 'move' method.
    def move(self):
        print(f"The {self.name} is driving 🚗.")


# The 'Plane' class also inherits from 'Vehicle'.
class Plane(Vehicle):
    # This is the Plane's specific implementation of the 'move' method.
    def move(self):
        print(f"The {self.name} is flying ✈️.")


# The 'Boat' class inherits from 'Vehicle' as well.
class Boat(Vehicle):
    # And here is the Boat's specific implementation of 'move'.
    def move(self):
        print(f"The {self.name} is sailing ⛵️.")


# --- Main Program ---
def main():
    # Create instances of our different vehicle classes.
    my_car = Car("Ford Mustang")
    my_plane = Plane("Boeing 747")
    my_boat = Boat("Sailboat")

    # Create a list containing all the vehicle objects.
    vehicles = [my_car, my_plane, my_boat]

    print("--- Polymorphism in action! ---")
    # Loop through the list of vehicles.
    # The same '.move()' method call will execute a different
    # version of the method depending on the object's type.
    for vehicle in vehicles:
        vehicle.move()

# This ensures the main function runs when the script is executed.
if __name__ == "__main__":
    main()
