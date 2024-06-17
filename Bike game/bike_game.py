import time
import random

class Bike:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def ride(self):
        self.distance += self.speed
        print(f"{self.name} is riding at {self.speed} km/h")

    def __str__(self):
        return f"{self.name} has traveled {self.distance} km"

def game():
    bike1 = Bike("Bike 1", 20)
    bike2 = Bike("Bike 2", 25)

    while True:
        print("\n" + "=" * 20)
        print("Current Distance:")
        print(bike1)
        print(bike2)
        print("=" * 20)

        bike1.ride()
        bike2.ride()

        time.sleep(1)  # wait for 1 second

        if bike1.distance >= 100:
            print("Bike 1 wins!")
            break
        elif bike2.distance >= 100:
            print("Bike 2 wins!")
            break

        # add some randomness to the game
        if random.randint(1, 10) == 5:
            bike1.speed += 5
            print(f"{bike1.name} got a speed boost!")
        elif random.randint(1, 10) == 7:
            bike2.speed += 5
            print(f"{bike2.name} got a speed boost!")

if __name__ == "__main__":
    game()







 