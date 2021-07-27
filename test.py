def get_number(prio):
    try:
        number = float(input(f"Give me the {prio} number: "))
        return number
    except ValueError:
        print("ValueError Please Try Again")
        return get_number(prio)


def get_operator(prio):
    accepted_operators = ['+', '-', '*', '/']
    operator = input(f"Enter {prio} operator: ")
    if operator in accepted_operators:
        return operator
    else:
        print("Wrong Operator Please Try Again")
        return get_operator(prio)


while True:
    num1 = get_number('first')
    op1 = get_operator('first')
    num2 = get_number('second')
    op2 = get_operator('second')
    num3 = get_number('third')
    if op1 == '+' and op2 == '+':
        print(f' {num1} + {num2} + {num3} = {num1 + num2 + num3}')
    elif op1 == '-' and op2 == '-':
        print(f' {num1} - {num2} - {num3} = {num1 - num2 - num3}')
    elif op1 == '*' and op2 == '*':
        print(f' {num1} * {num2} * {num3} = {num1 * num2 * num3}')
    elif op1 == '/' and op2 == '+':
        print(f' ({num1} / {num2}) + {num3} = {(num1 / num2) + num3}')
    else:
        print("Invalid Operation")
    cont = input("Press: Enter to Continue or type: 'Exit' to finish")
    if cont.lower() == 'exit':
        print("\nRequested Exit Operation")
        break

