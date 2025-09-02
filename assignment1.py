# This is the parent class. It defines the basic attributes and methods
# that all superheroes will have.
class Superhero:
    # The constructor method, '__init__', is called when a new object is created.
    # It initializes the object's attributes with the values passed in.
    def __init__(self, name, secret_identity, power):
        # Attributes are variables associated with an object.
        self.name = name
        self.secret_identity = secret_identity
        self.power = power

    # A method is a function that belongs to an object.
    def use_power(self):
        """A general method for using a superhero's power."""
        print(f"{self.name} uses their {self.power}!")

    def reveal_identity(self):
        """Reveals the hero's secret identity."""
        print(f"The hero known as {self.name} is secretly {self.secret_identity}.")


# This is a child class, 'FlyingHero', that inherits from 'Superhero'.
# It automatically gets all the attributes and methods of the parent class.
class FlyingHero(Superhero):
    # This is the constructor for the child class.
    # It takes all the parent class's attributes, plus its own unique ones.
    def __init__(self, name, secret_identity, power, flight_speed):
        # The 'super()' function calls the constructor of the parent class.
        # This initializes the inherited attributes.
        super().__init__(name, secret_identity, power)
        # This is the new, unique attribute for FlyingHero objects.
        self.flight_speed = flight_speed

    # This is a new method unique to the child class.
    def fly(self):
        """A method for flying, specific to this class."""
        print(f"{self.name} soars through the sky at a speed of {self.flight_speed} mph.")

    # This is an example of polymorphism. We are overriding the parent's
    # 'use_power' method with a new, more specific implementation.
    def use_power(self):
        """A special method for using a flying hero's power."""
        print(f"**WHOOSH!** {self.name} unleashes a powerful {self.power} attack!")


# --- Example Usage ---

# Creating an instance of the base Superhero class
print("--- Base Superhero ---")
captain_america = Superhero("Captain America", "Steve Rogers", "super-strength")
captain_america.use_power()
captain_america.reveal_identity()
print()

# Creating an instance of the inherited FlyingHero class
print("--- Flying Hero ---")
superman = FlyingHero("Superman", "Clark Kent", "heat vision", 1000)
# This calls the new, specialized 'use_power' method.
superman.use_power()
# This calls the new 'fly' method.
superman.fly()
# This calls the 'reveal_identity' method inherited from the parent class.
superman.reveal_identity()
