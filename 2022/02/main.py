POINTS = {"X": 1, "Y": 2, "Z": 3, "lose": 0, "draw": 3, "win": 6}

cleaned_records = []
total_score = 0


def decode_points(key):
    return POINTS.get(key)


with open("input.txt") as f:
    records = f.readlines()

for record in records:
    stripped = record.strip("\n")
    cleaned_records.append(stripped.split(" "))

for record in cleaned_records:
    total_score += decode_points(record[1])
    if record[1] == "X":
        if record[0] == "A":
            total_score += decode_points("draw")
        elif record[0] == "B":
            total_score += decode_points("lose")
        elif record[0] == "C":
            total_score += decode_points("win")
    elif record[1] == "Y":
        if record[0] == "A":
            total_score += decode_points("win")
        elif record[0] == "B":
            total_score += decode_points("draw")
        elif record[0] == "C":
            total_score += decode_points("lose")
    elif record[1] == "Z":
        if record[0] == "A":
            total_score += decode_points("lose")
        elif record[0] == "B":
            total_score += decode_points("win")
        elif record[0] == "C":
            total_score += decode_points("draw")

print(f"Total Score: {total_score}")

# reset score for part two
total_score = 0

for record in cleaned_records:
    if record[0] == "A":
        if record[1] == "X":
            total_score = total_score + decode_points("lose") + decode_points("Z")
        elif record[1] == "Y":
            total_score = total_score + decode_points("draw") + decode_points("X")
        elif record[1] == "Z":
            total_score = total_score + decode_points("win") + decode_points("Y")
    if record[0] == "B":
        if record[1] == "X":
            total_score = total_score + decode_points("lose") + decode_points("X")
        elif record[1] == "Y":
            total_score = total_score + decode_points("draw") + decode_points("Y")
        elif record[1] == "Z":
            total_score = total_score + decode_points("win") + decode_points("Z")
    if record[0] == "C":
        if record[1] == "X":
            total_score = total_score + decode_points("lose") + decode_points("Y")
        elif record[1] == "Y":
            total_score = total_score + decode_points("draw") + decode_points("Z")
        elif record[1] == "Z":
            total_score = total_score + decode_points("win") + decode_points("X")


print(f"Score Needed To Win: {total_score}")
