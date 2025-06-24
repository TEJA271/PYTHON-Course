# Exercise 18: Multiple Inheritance - Battery and GPS Tracker
# Create classes Battery and GPS with respective methods charge and location. Derive a SmartPhone class that inherits both functionalities.

class Battery:
    def charge(self):
        print("Battery is charging...")

class GPS:
    def location(self):
        print("GPS is showing location...")

class SmartPhone(Battery, GPS):
    pass



phone = SmartPhone()
phone.charge()
phone.location()
