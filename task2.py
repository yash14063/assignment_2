# Task 2: Sum of Integers from 1 to 50 Using a Loop

def calculate_sum():
    total_sum = 0
    for i in range(1, 51):
        total_sum += i
    print(f"The sum of integers from 1 to 50 is: {total_sum}")

if __name__ == "__main__":
    calculate_sum()
