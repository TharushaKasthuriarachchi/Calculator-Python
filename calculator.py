def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(e)

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

def select_op(choice, history):
    if choice == '#':
        return -1
    elif choice == '$':
        history.clear()
        return 0
    elif choice == '?':
        if not history:
            print("No past calculations to show")
        else:
            for record in history:
                print(record)
        return 1
    elif choice in ('+', '-', '*', '/', '^', '%'):
        while True:
            num1s = input("Enter first number: ")
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1

            try:
                num1 = float(num1s)
                break
            except:
                print("Not a valid number, please enter again")
                continue

        while True:
            num2s = input("Enter second number: ")
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:
                num2 = float(num2s)
                break
            except:
                print("Not a valid number, please enter again")
                continue

        result = 0.0
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)
        else:
            print("Something Went Wrong")

        last_calculation = "{0} {1} {2} = {3}".format(num1, choice, num2, result)
        history.append(last_calculation)
        print(last_calculation)

    else:
        print("Unrecognized operation")
    return 1

history = []
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")

    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if select_op(choice, history) == -1:
        # program ends here
        print("Done. Terminating")
        exit()
