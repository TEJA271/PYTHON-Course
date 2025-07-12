# Define the BMW class
class BMW:
    def start_engine(self):
        print("BMW engine started with a roar.")

    def stop_engine(self):
        print("BMW engine stopped smoothly.")

    def drive(self):
        print("Driving the BMW on the highway.")

# Define the Ferrari class
class Ferrari:
    def start_engine(self):
        print("Ferrari engine started with a scream.")

    def stop_engine(self):
        print("Ferrari engine shut down like a beast at rest.")

    def drive(self):
        print("Driving the Ferrari on the racetrack.")

# Function to demonstrate polymorphism
def test_drive(car):
    car.start_engine()
    car.drive()
    car.stop_engine()

if __name__ == "__main__":
    bmw_car = BMW()
    ferrari_car = Ferrari()

    print("Testing BMW:")
    test_drive(bmw_car)

    print("\nTesting Ferrari:")
    test_drive(ferrari_car)
