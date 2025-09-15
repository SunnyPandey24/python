# ❌ Invalid: sets cannot contain lists because lists are mutable
# s = {[1, 2], [3, 4]}  

# ✅ But we can use tuples (immutable)
s = {(1, 2), (3, 4)}
print(s)
