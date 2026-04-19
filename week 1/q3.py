a = int(input("Give a: "))
b = int(input("Give b: "))

if a > b:
    print("Error, a must be less than b")
else:
    current = a

    while current <= b:
        print(current, end=" ")
        current = current + 1

    print()
    