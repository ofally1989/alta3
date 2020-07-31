#!/usr/bin/bash env python3

def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def mul(num1,num2):
    return(num1*num2)
def div(num1,num2):
    return(num1/num2)
print("  menu   ")
print("1.  +    ")
print("2.  -    ")
print("3.  *    ")
print("4.  /    ")
x=int(input("Enter first value : "))
y=int(input("Enter second value: "))
choice=input("Enter your choices( 1/2/3/4: ")
if choice == 1:
    print(x + y)
elif choice == 2:
    print(x - y)
elif choice == 3:
    print(x*y)
elif choice == 4:
    print(x / y)
else:
    print("wrong choice")



