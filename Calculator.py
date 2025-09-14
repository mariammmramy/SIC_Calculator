def divide(a,b):
	result = a / b
	return result
print(f"9 divided 3 is {divide(9,3)}")
print(f"10 divided 2 is {divide(10,2)}")
from addition import add_numbers
from Multiplication import Multi
def subtract(x, y):
    return x - y
def main():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    op=input("Enter operation symbol")

    match(op):
        case "-":
            result=subtract(num1,num2)
        case "+":
            result=add_numbers(num1,num2)
        case "*":
            result=Multi(num1,num2) 
        case "/":
            result=divide(num1,num2)

    print(f"Result is: {result}")

if __name__ == "__main__":
    main()


