marks1 = int(input("Enter the Number in Sub1 : "))
marks2 = int(input("Enter the Number in Sub2 : "))
marks3 = int(input("Enter the Number in Sub3 : "))

# Calculate total percentage out of 300 marks
total_percentage = (100 * (marks1 + marks2 + marks3) / 300)

# Check conditions for passing
if (total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are Passed", total_percentage)

else:
    print("You are Failed, try next year!", total_percentage)
