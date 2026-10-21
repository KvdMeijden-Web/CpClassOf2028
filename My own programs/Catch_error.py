try: 
    number = float(input("input number"))
    result = 10/number
    print(result)
except ValueError:
    print("please enter a number")
except ZeroDivisionError:
    print("cannot divide by 0")