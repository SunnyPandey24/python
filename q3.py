s = {1, 2, 3, 4, 5}

s.remove(3)   # Removes element, error if not found
print(s)

s.discard(10) # No error if element not found
print(s)

s.pop()       # Removes a random element
print(s)

s.clear()     # Empty the set
print(s)
