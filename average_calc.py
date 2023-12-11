#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: December 11th, 2023
# this program generates 10 numbers between 0 to 100 and calculates the average of them.
import random

MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100


def main():
    # Generate random numbers
    numbers = generate_random_numbers()

    # Print the numbers
    print("Generated Numbers:")
    print(numbers)

    # Calculate the average
    average = calculate_average(numbers)

    # Display the average
    print(f"\nAverage: {average}")


def generate_random_numbers():
    # Generate the 10 random numbers
    numbers = []
    for _ in range(MAX_ARRAY_SIZE):
        number = random.randint(MIN_NUM, MAX_NUM)
        numbers.append(number)

    return numbers


def calculate_average(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    # Formula for the average numbers
    average = total / count
    return average


if __name__ == "__main__":
    main()
