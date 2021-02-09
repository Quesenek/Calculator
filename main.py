import os

def master():
    
    clear = lambda: os.system('cls')

    print("Enter the first number to be calculated")
    inp = float(input())
    clear()

    print("Enter the second number to be calculated")
    inp2 = float(input())
    clear()

    print("Enter enter + - * / %, for what you want to be done")
    inpOp = input()
    clear()

    print("The total is: %s" % (str(calculation(inp, inp2, inpOp))))
    
def calculation(first, second, operator):
    total = 0
    if(operator == "+"):
        total = first + second
    elif(operator == "-"):
        total = first - second
    elif(operator == "*"):
        total = first * second
    elif(operator == "/"):
        total = first / second
    elif(operator == "%"):
        total = first % second
    
    if(float(total).is_integer()):
        total = int(total)
    return total

def main():
    master()

if __name__ == "__main__":
    main()