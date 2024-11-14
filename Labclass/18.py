def divide_numbers(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
print(divide_numbers(10,2))
print(divide_numbers(10,0))