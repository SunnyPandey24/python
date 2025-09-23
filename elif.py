# Take input from user and convert it into an integer
a = int(input("Enter the age:"))

# Check if the entered age is greater than or equal to 18
if(a >= 18):
    # If age is 18 or more
    print("You are above the age of consent")
    print("Good for you")

elif(a < 0):
    # Negative ages are invalid
    print("You are entering wrong")

elif(a == 0):
    # Age 0 is also not valid
    print("You are entering invalid age")

else:
    # If age is positive but less than 18
    print("You are not above the age of consent")
