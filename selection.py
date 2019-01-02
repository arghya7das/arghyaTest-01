num1 =  int(input("Please enter First number:"))
num2 = int(input("pleasse enter Second number: "))
if num1 > num2:
    print("The First number is greater:  " + str(num1))
    print("The diffirence is: "+ str(num1-num2))
elif num1 < num2:
    print("The Second number is greater: "+ str(num2))
    print("The diffirence is: " + str(num1 - num2))
else:
    print("Both numbers are equal")
