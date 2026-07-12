def addtion():
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    print(f"Sum of given number : {num1+num2}")

def subtraction():
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    print(f"Sum of given number : {num1-num2}")

def multiplication():
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    print(f"Sum of given number : {num1*num2}")

def divition():
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    print(f"Sum of given number : {num1//num2}")

def exite():
    print("Ab tum bhar aa gye ho")

while True:
    print("1. Addtion")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divition")
    print("5. Exite")

    n=int(input("Enter the number, What Do You Want To You  "))
    if n==1:
        addtion()
    elif n==2:
        subtraction()
    elif n==3:
        multiplication()
    elif n==4:
        divition()
    elif n==5:
        exite()
        break
    else:
        print("Plese Enter the valid no")