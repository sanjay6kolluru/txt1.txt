def create_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")
def create_operation():
    operation=['+','-','*','/']
    while True:
        op=input("enter operation (+,-,*,/):")
        if op in operation:
            return op
        else:  
            print("Invalid operation!,enter the operation(+,-,*,/)")
def calculate(num1,num2,op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        if num2%2==0:
            return "Error ;division by zero!"
        return num1 / num2
def main():
    print("SIMPLE PYTHON CALCULATOR")
    num1=create_number("Enter a first number")
    num2=create_number("Enter a second number")
    op=create_operation()
    result=calculate(num1,num2,op)
    
    print(f"Result:{num1}{op}{num2}={result}")
    
if __name__ == "__main__":
    main()
