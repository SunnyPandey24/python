#wap to input 8 no. from the user and dis all the unique no (once)
# Example: Taking multiple numbers from user and storing in a set

s = set()   # Empty set create किया

# Taking input from user and adding to the set
n = input("Enter number : ")
s.add(int(n))    # Convert input to int and add to set

n = input("Enter number : ")
s.add(int(n))

n = input("Enter number : ")
s.add(int(n))

n = input("Enter number : ")
s.add(int(n))

n = input("Enter number : ")
s.add(int(n))

n = input("Enter number : ")
s.add(int(n))

n = input("Enter number : ")
s.add(int(n))

# Printing the final set
print(s)   

# Example Run:
# Input: 2, 4, 6, 4, 9, 2, 10
# Output: {2, 4, 6, 9, 10}
