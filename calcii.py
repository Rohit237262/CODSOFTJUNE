num1=int(input("Enter the first number\n"))
oper=input("enter operator(eg:+,-,*,/) :\n")
num2=int(input("Enter the second number\n"))
if oper=="+":
    print("Addition of the number is :\n",num1+num2)
elif oper=="-":
    print("Subtraction of the number is\n:",num1-num2)
elif oper=="*":
    print("Multiple of the number is :\n",num1*num2)
elif oper=="/":
    print("Division of the numer is :\n",num1/num2)
elif oper=="%":
    print("Remainder of the number is\n:",num1%num2)
else:
    print("🛹👍Invalid operation 👍🛹")