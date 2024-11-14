def divide_numbers(num1,num2):
    try:
        result=float(num1)/float(num2)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Invalid input. Please enter numbers."
print(divide_numbers(10,2))
print(divide_numbers(10,2))
print(divide_numbers(10,'a'))
print(divide_numbers('b',2))