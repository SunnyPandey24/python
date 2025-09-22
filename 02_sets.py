# Set example with mixed data types
s = {1, 5, 65, 54, 54, 5.5, 4, 25, "Sunny"}  
# यहाँ set में integer, float और string values हैं
# Duplicates (जैसे 54) अपने आप हट जाते हैं

e = set()   # Empty set बनाने का सही तरीका

print(s, type(s))
# Example Output: {1, 65, 4, 5, 5.5, 54, 25, 'Sunny'} <class 'set'>
