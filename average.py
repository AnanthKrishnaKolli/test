import random

def generate_random_numbers(n):
    random_numbers = []
    for i in range(n):
        random_numbers.append(random.randint(1, 100))
    return random_numbers

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    average = total / len(numbers)
    return average

def main():

    n = int(input("Enter the number of random numbers to generate: "))
    if n <= 0:
        raise ValueError("Please enter a positive number.")
    
    random_numbers = generate_random_numbers(n)
    
    if random_numbers:
        average = calculate_average(random_numbers)
        print(f"Generated numbers: {random_numbers}")
        print(f"Average of generated numbers: {average:.2f}")
    else:
        print("No numbers generated.")

if __name__ == "__main__":
    main()
