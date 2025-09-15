A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7}

print(A.issubset(B))   # True
print(B.issuperset(A)) # True
print(A.isdisjoint(C)) # True (no common elements)
