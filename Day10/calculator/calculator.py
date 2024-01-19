import art

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate():
    print(art.calc)
    print(art.logo)
    end = False
    num1 = int(input("Whats the first number? "))

    for op in operations:
        print(op)
    op_symbol = input("Pick an operation from the above: ")

    num2 = int(input("Whats the second number? "))

    calculation = operations[op_symbol]
    answer= calculation(num1, num2)

    print(f"{num1} {op_symbol} {num2} = {answer}")
    while not end:
        ask = input("Do you want to calculate further: y or n ")
        if ask == 'n':
            end = True
            calculate()

        num1 = answer
        for op in operations:
            print(op)
        op_symbol = input("Pick an operation from the above: ")
        num2 = int(input("Whats the next number? "))

        calculation = operations[op_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {answer}")
    
  
calculate()
