# wap to find the gretest of four number entrred by te user
a = int(input("Enter the Number 1:-"))
b = int(input("Enter the Number 2:-"))
c = int(input("Enter the Number 3:-"))
d = int(input("Enter the Number 4:-"))

if (a > b and a > c and a > d):
    print("Number 1 is Greatest")

if (b > a and b > c and b > d):
    print("Number 2 is Greatest")

if (c > b and c > a and c > d):
    print("Number 3 is Greatest")

else:  # small correction: should check against c also
    print("Number 4 is Greatest")
