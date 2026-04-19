file = open("expenses.txt", "a")

answer = "yes"

while answer == "yes":
    category = input("Enter category: ")
    amount = input("Enter amount: ")

    file.write(category + ", " + amount + "\n")
    answer = input("Do you want to continue? (yes/no) ")