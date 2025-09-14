
def subtract(x, y):
    return x - y
def main():
    num1=input("Enter first number: ")
    num2=input("Enter second number: ")
    op=input("Enter operation symbol")

    match(op):
        case "-":
            result=subtract(num1,num2)
    

    print("Result is: {result}")

