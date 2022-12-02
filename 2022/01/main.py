with open("input.txt", "r") as f:
    records = f.readlines()

most_calories, total, top_three = 0, 0, 0
elves = []

for record in records:
    if record == "\n":
        total = 0
    else:
        total += int(record)

    if total > most_calories:
        most_calories = total

    elves.append(total)

elves.sort(reverse=True)

for count in elves[0:3]:
    top_three += count

print(f"Most Calories: {most_calories}")
print(f"Total Calories: {top_three}")
