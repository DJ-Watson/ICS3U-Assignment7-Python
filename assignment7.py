#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: December 2019
# This program reorders a list

import random


def main():
    # function holds list

    # variables
    numbers = []
    order = []

    # input
    print("numbers are: ")
    for loop_c in range(0, 5):
        single_number = random.randint(0, 100)
        numbers.append(single_number)
        print("{}".format(single_number))
    print("")

    numinput = int(input("input number of times to move list (0-4): "))
    for loop_c2 in range(0, 5):
        single_order = numinput
        if numinput > 3:
            numinput -= 4
            order.append(single_order)
        else:
            numinput += 1
            order.append(single_order)
    numbers = [numbers[i] for i in order]

    print("new numbers are: ")
    for loop_c3 in range(0, 5):
        print(numbers[loop_c3])


if __name__ == "__main__":
    main()
