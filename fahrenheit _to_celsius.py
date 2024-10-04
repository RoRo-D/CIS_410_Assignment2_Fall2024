#!/usr/bin/env python3

import conversions as c

def display_welcome():
    print("Fahrenheit and Celsius Convertor")
    print()

def display_menu():
    print("Conversion Menu")
    print("A. Fahrenheit to Celsius")
    print("B. Celsius to Fahrenheit")

def main():
    display_welcome()

    again = "y"
    while again.lower() == "y":

        display_menu()
        choice = input("Select a conversion (A/B): ")
        print()

        if choice == "A":
            fahrenheit = round(input("Enter fahrenheit: "))
            celsius = c.to_celsius(fahrenheit)
            print(round(celsius, 0), "degress celsius")
        elif choice == "B":
            celsius = round(input("Enter celsius: "))
            fahrenheit = c.to_fahrenheit(celsius)
            print(round(fahrenheit, 0), "degress fahrenheit")
        else:
            print("You did not enter a valid selection. Please try again.")
        print()

        again = input("Would you like to perform another conversion? (y/n): ") 
        print() 

        print("Thank you, See you next time!")  


if __name__ == "__main__":
    main()