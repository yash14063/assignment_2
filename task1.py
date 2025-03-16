# Task 1: Check if a Number is Even or Odd

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    check_even_odd(number)
