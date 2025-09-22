# Example of union operation in sets

s1 = {1, 3, 54, 6}           # First set
s2 = {7, 43, 75, 45, 3}      # Second set (notice 3 is common in both)

# union() → combines both sets and removes duplicates
print(s1.union(s2))  
# Output: {1, 3, 6, 7, 43, 75, 45, 54}
