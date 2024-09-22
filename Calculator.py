import math
print("""Addition +
Subtration -
multiplication *
Division /
Factorial !
square ^
Square root #
percentage %
sin
cos
tan""")
a=input("Enter the desired function:--> ")
if a=='+':
    p=int(input("enter 1st number:--> "))
    q=int(input("Enter 2nd number:--> "))
    print(p+q)
elif a=='-':
    p=int(input("enter 1st number:--> "))
    q=int(input("Enter 2nd number:--> "))
    print(p-q)
elif a=='*':
    p=input("enter 1st number:--> ")
    q=input("Enter 2nd number:--> ")
    print(p*q)
elif a=='/':
    p=input("enter 1st number:--> ")
    q=input("Enter 2nd number:--> ")
    print(p/n)
elif a=='!':
    p=int(input("enter the number:--> "))
    print(math.factorial (p))
elif a=="^":
    p=int(input("enter the number:--> "))
    print(p*p)
elif a=='#':
    q=int(input("Enter the number:--> "))
    print(math.sqrt(q))
elif a=='%':
    p=int(input("enter 1st number:--> "))
    q=int(input("Enter 2nd number:--> "))
    print(p/q*100)
elif a=='sin':
    p=int(input("enter the angle:--> "))
    print(math.sin(math.radians(p)))
elif a=='cos':
    p=int(input("enter the angle:--> "))
    print(math.cos(math.radians(p)))
elif a=="tan":
    p=int(input("Enter the angle:-->"))
    print(math.tan(math.radians(p)))

