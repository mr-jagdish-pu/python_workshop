#A CALC USINg SWITCH

def calculater():
    pref = input("Enter operator (+,-,*,/): ")
    if(pref == '+'):
        num1 = int(input("Enter first number: "))

        num2 = int(input("Enter second number: "))
        
        print(num1 + num2)
    elif(pref == '-'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1 - num2)
    elif(pref == '*'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1 * num2)
    elif(pref == '/'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1 / num2)
    else:
        print("Invalid operator")
calculater()
