def calculate_division(a, b):
    result = a / b
    return result

def perform_calculation(x, y):
   
    division_result = calculate_division(x, y)
    print(f"Result of division: {division_result}")
    
    if division_result == "Infinity":
        raise Exception("Division by zero occurred!")
    
    return division_result


def main():
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        
        result = perform_calculation(num1, num2)
        
        if result < 0:
            raise ValueError("Negative result obtained!")
        
        print("Calculation completed successfully.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
