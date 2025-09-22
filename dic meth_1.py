# Example of dictionary with string and integer keys

marks = { 
    "Sunny": 98,      # Key = "Sunny", Value = 98
    "Rohan": 74,      # Key = "Rohan", Value = 74
    "Chandan": 76,    # Key = "Chandan", Value = 76
    0: "bharat"       # Key = 0 (integer), Value = "bharat"
}

# .items() returns all key-value pairs as a list of tuples
print(marks.items())
# Output: dict_items([('Sunny', 98), ('Rohan', 74), ('Chandan', 76), (0, 'bharat')])
