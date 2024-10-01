def main():
    value1 = int(input("Enter an integer value: "))
    value2 = int(input("Enter an integer value: "))
    value3 = int(input("Enter an integer value: "))
    
    max_value = maximum_three(value1, value2, value3)
    min_value = minimum_three(value1, value2, value3)
    avg_value = average_three(value1, value2, value3)
    
    print(f"The Maximum of {value1} {value2} {value3} is {max_value}")  
    print(f"The Minimum of {value1} {value2} {value3} is {min_value}")  
    print(f"The Average of {value1} {value2} {value3} is {avg_value:.1f}") 

def maximum_three(value1, value2, value3):
    return max(value1, value2, value3)


def minimum_three(value1, value2, value3):
    return min(value1, value2, value3)


def average_three(value1, value2, value3):
    avg = (value1 + value2 + value3) / 3
    return avg


if __name__ == "__main__":
    main()
