a = int(input("Enter the number: "))
temp = 2
if (a % temp != 0):
    if (a % 1 == 0 and a % a == 0):
        print(a, "is a prime number")
else:
    print(a, "is not a prime number")
