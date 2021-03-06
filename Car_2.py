class Car_2():
    """A simple attempt to represent a car """

    def __init__(self, make, model, year):
        """Initialize attributrs to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!(not legally at least ;))")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


"""
my_new_car = Car_2('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(10)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
"""


class ElectricCar(Car_2):
    """Represent aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize the attributes specific to an electric car.
        """

        super().__init__(make, model, year)
        self.battery = Battery()

    def upgrade_battery(self):
        if self.battery.battery_size < 85:
            self.battery.battery_size = 85


class Battery():
    """ A simple attempt to model a battery for an electric car """

    def __init__(self, battery_size=70):
        """Initialize battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a statement describing the battery size """
        print("This car has a " + str(self.battery_size) + "-Kwh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

"""
my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
"""

old_tesla = ElectricCar('Tesla','Roadster',2010)
#initial battery
print(old_tesla.get_descriptive_name())
old_tesla.battery.get_range()
#battery upgrade
old_tesla.upgrade_battery()
old_tesla.battery.get_range()