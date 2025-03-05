"""
This program finds the volume of a tire by asking for user inputs.

In addition to the base requirements, this program determines the cost of a single tire using an if elif else statement to determine price based on size of the tire.
Users will see how much an individual tire costs after providing the requested inputs.

All new entries are written to the text file volumes.txt
"""

import math
import os
from datetime import datetime

def volume_of_a_tire():
    # Get today's date
    current_date = datetime.now(tz=None)

    # User inputs for volume
    width = int(input("What is the width of the tire? "))
    aspect_ratio = int(input("What is the aspect ratio of the tire? "))
    diameter = int(input("What is the diameter of the wheel in inches? "))

    # Equation to get volume
    volume = round(((math.pi * (width ** 2) * aspect_ratio * ((width * aspect_ratio) + (2540 * diameter))) / 10000000000), 2)

    # Add inputs to volumes.txt
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume}\n")
    
    def categorize_tire_cost(width):
        if width <= 155:
            return "$100 per tire"
        elif 156 <= width <= 195:
            return "$150 per tire"
        elif 196 <= width <= 225:
            return "$200 per tire"
        elif 226 <= width <= 275:
            return "$325 per tire"
        else:
            return "$400 per tire"

    return f"{volume} liters, {categorize_tire_cost(width)}"

# Get today's date
# current_date = datetime.now(tz=None)

# Clear console at the beginning of running the script 
os.system('clear')
# Display result of volume_of_a_tire()
print(f"{volume_of_a_tire()}")
# Save results to volumes.txt
# with open("volumes.txt", "a") as file:
#     file.write(f"{current_date}")