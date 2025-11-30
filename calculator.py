def add(a,b):
    return a+b

def sub(c,d):
    return c-d

def mul(e,f):
    return e*f

def div(g,h):
    return g/h

print("Welcome to the calculator!")
operator=int(input("Choose an operator\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n:"))
if operator not in [1,2,3,4]:
    print("Invalid operator!")
else:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    if operator==1:
        print(num1,"+",num2,"=",add(num1,num2))
    elif operator==2:
        print(num1,"-",num2,"=",sub(num1,num2))
    elif operator==3:
        print(num1,"x",num2,"=",mul(num1,num2))
    elif operator==4:
        print(num1,"/",num2,"=",div(num1,num2))
