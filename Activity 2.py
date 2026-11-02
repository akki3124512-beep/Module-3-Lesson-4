try:
    num1, num2 = eval(input("Enter 2 numbers, seperated by a comma: "))
    print(f"{num1} divided by {num2} is: ", num1/num2)
except ZeroDivisionError:
    print("You can't divide by zero!")
except SyntaxError:
    print("You missed a comma in between the numbers!")
except:
    print("The numbers dont work!")
else:
    print("No exceptions!")
finally:
    print("This statement will show no matter what!")