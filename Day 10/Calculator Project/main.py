
import art

def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1, n2):
    return n1*n2
def div(n1,n2):
    return n1/n2


operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def calculate():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("first number"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an Operation")
        num2 = float(input("second number"))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2}= {answer}")

        choice = input(f"Type 'y  to continue calculating with{answer}, or type 'n ' to start a new calculation")

        if choice == "y":
            num1 = answer
        else :
            should_accumulate = False
            print("\n" * 20)
            calculate()

calculate()