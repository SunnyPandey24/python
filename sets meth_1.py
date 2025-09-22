# Example of adding element in a set

s = {1, 5, 65, 54, 54, 5.5, 4, 25, "sunny"}  
# Duplicate 54 अपने आप हट जाएगा

s.add(342)   # Set में नया element add किया

print(s, type(s))
# Example Output: {1, 65, 4, 5, 5.5, 54, 25, 'sunny', 342} <class 'set'>
