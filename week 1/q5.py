total = 0.0
more = "y"

while more == "y":
    price = float(input("Item price: "))
    total = total + price

    more = input("Have more items? (y/n) ")

print("Total:", total)

