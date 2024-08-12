def adder():
    try:
        a = int(input("Enter number one"))
        b = int(input("Enter number two"))
    except ZeroDivisionError:
        print("Second no is zero")
    except:
        print("Number is excepted, no string")