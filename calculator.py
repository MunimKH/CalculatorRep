print("python calculator")
value1=int(input("Enter the 1st number !!! "))
value2=int(input("Enter the 2nd number !!! "))
print("\n Here are some operation you can perform !!! \n 1) sum \n 2) subtract \n 3) divide \n 4) multiply")
function=input("What operation you want to perform ? ").lower()
print(function)

if function == "sum":
    answer= value1+value2
elif function == "subtract" :
    answer = value1 - value2
elif function == "divide" :
    answer = value1 / value2
elif function == "multiply" :
    answer = value1 * value2
else:
    print("Wrong operation !!! ")

print (f"The {function} of {value1} and {value2} is : {answer}")

