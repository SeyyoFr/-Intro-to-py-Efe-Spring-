file = open("expenses.txt", "r")

category_name = input("Enter category to calctulate totat: ")
total = 0

for line in file:
    line = line.strip()
    parts = line.split(", ")

    category = parts[0].strip()
    amount = float(parts[1].strip())

    if category == category_name:
        total = total + amount

file.close()

print("Total expense for " + category_name + " is:", total)
