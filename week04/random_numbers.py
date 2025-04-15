import random


numbers_list = []

def main():
    # global generated_list
    numbers_list = create_random_list(6)
    print(numbers_list)
    print()
    append_random_numbers(numbers_list)
    print(numbers_list)
    print()
    append_random_numbers(numbers_list, 5)
    print(numbers_list)
    


def create_random_list(quantity):
    random_list = []
    for i in range(quantity):
        random_int = round(random.uniform(1, 100), 1)
        random_list.append(random_int)
    return random_list


def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        random_int = round(random.uniform(1, 100), 1)
        numbers_list.append(random_int)

main()

