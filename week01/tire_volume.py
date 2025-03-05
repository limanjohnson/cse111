import math
import os

def volume_of_a_tire():
    width = int(input("What is the width of the tire? "))
    aspect_ratio = int(input("What is the aspect ratio of the tire? "))
    diameter = int(input("What is the diameter of the wheel in inches? "))

    volume = round(((math.pi * (width ** 2) * aspect_ratio * ((width * aspect_ratio) + (2540 * diameter))) / 10000000000), 2)

    return volume

os.system('clear')
print(f"{volume_of_a_tire()} liters")