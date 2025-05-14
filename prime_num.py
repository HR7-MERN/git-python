a = input("Plpease enter a number: ")
a = int(a)
posb = 0
for i in range(1, a+1):
    if (a % i == 0):
        posb = posb + 1
        continue
if posb <= 2:
    print("Prime number")
else:
    print("Not a prime number")
