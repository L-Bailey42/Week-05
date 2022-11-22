#!/usr/bin/env python3


if __name__ == "__main__":
    number = input("Enter a number: ")
    number = int(number)
    print("The numbered entered was", number)

    if (number % 10) == 0:
        print("That is an even number. That number is divisible by 10.")
    elif (number % 2) != 0:
        print("That is an odd number. That number is not divisible by 10.")
    else:
        print("That is an even number. That number is not divisible by 10.")

