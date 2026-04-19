file = open("expenses.txt", "r")

totals = {}

for line in file:
    line = line.strip()
    parts = line.split(", ")
        
    if len(parts) < 2:
        continue

    category = parts[0].strip()
    amount = float(parts[1].strip())

    if category in totals:
        totals[category] = totals[category] + amount
    else:
        totals[category] = amount

file.close()

sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)

for item in sorted_totals:
    print(item[0], item[1])

    