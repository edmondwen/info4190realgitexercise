def calculate(num1, num2, op):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    else:
        print("The operator '" + op + "' is not correct")
        result = None
    return result