a = 31
t = type(a)  #class <int>
print(t)
 

a = 32.4
t = type(a)  #class <float>
print(t)

a = "Harry"
t = type(a)  #class <string>
print(t)

a = "32.5"
b = float(a) # a but the type should br float
t = type(b)  #class <int>
print(t)