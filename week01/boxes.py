import math

num_of_items = int(input("Enter the number of items: "))
num_of_items_per_box = int( input("Enter the number of items per box: "))


boxes_needed = math.ceil(num_of_items/num_of_items_per_box)

print(f"For {num_of_items} you will need {boxes_needed} boxes.")