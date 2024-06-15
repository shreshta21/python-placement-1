try:
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    result= num1/num2
    print("Result:",result)
    
except ValueError:
    print("Invalid input,Please enter numeric values.")
    
except ZeroDivisionError:
    print("Error:Cannot divide by zero.")

else:
    print("No exception occured")
    
finally:
    print("End of program")