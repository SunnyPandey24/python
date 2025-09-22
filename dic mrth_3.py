# Example of updating a dictionary

marks = { 
    "Sunny": 98,      # Key = "Sunny", Value = 98
    "Rohan": 74,      # Key = "Rohan", Value = 74
    "Chandan": 76,    # Key = "Chandan", Value = 76
    0: "bharat"       # Key = 0 (integer), Value = "bharat"
}

# update() method se dictionary modify hoti hai
marks.update({"Chandan": 83, "Renuka": 72})

# Print the updated dictionary
print(marks)
# Output: {'Sunny': 98, 'Rohan': 74, 'Chandan': 83, 0: 'bharat', 'Renuka': 72}
