def main():
    try:
        value1 = int(input("Enter the first integer value: "))
        value2 = int(input("Enter the second integer value: "))
        value3 = int(input("Enter the third integer value: "))
    except ValueError:
        print("Invalid input! Please enter integer values only.")
        return
    
    max_value = maximum_three(value1, value2, value3)
    min_value = minimum_three(value1, value2, value3)
    avg_value = average_three(value1, value2, value3)
    
    print(f"The Maximum of {value1}, {value2}, {value3} is {max_value}")  
    print(f"The Minimum of {value1}, {value2}, {value3} is {min_value}")  
    print(f"The Average of {value1}, {value2}, {value3} is {avg_value:.1f}") 

def maximum_three(value1, value2, value3):
    """Returns the maximum of three values."""
    return max(value1, value2, value3)

def minimum_three(value1, value2, value3):
    """Returns the minimum of three values."""
    return min(value1, value2, value3)

def average_three(value1, value2, value3):
    """Returns the average of three values."""
    return (value1 + value2 + value3) / 3

if __name__ == "__main__":
    main()
