import string

LOWERCASE_OFFSET = 96
UPPERCASE_OFFSET = 38

sum_of_priorities = 0

with open("input.txt") as f:
    records = f.readlines()

cleaned_records = [record.strip() for record in records]
compartment_errors = []

for record in cleaned_records:
    compartment_index = len(record) // 2
    first_compartment = record[:compartment_index]
    second_compartment = record[compartment_index:]

    for letter in first_compartment:
        if letter in second_compartment:
            compartment_errors.append(letter)
            break


for error in compartment_errors:
    if error in string.ascii_lowercase:
        sum_of_priorities += ord(error) - LOWERCASE_OFFSET
    elif error in string.ascii_uppercase:
        sum_of_priorities += ord(error) - UPPERCASE_OFFSET

print(f"Sum of Priorities (Pt. 1): {sum_of_priorities}")

common_items = []
sum_of_priorities = 0

for i in range(0, len(cleaned_records), 3):
    for item in cleaned_records[i]:
        if item in cleaned_records[i + 1] and item in cleaned_records[i + 2]:
            common_items.append(item)
            break

for item in common_items:
    if item in string.ascii_lowercase:
        sum_of_priorities += ord(item) - LOWERCASE_OFFSET
    elif item in string.ascii_uppercase:
        sum_of_priorities += ord(item) - UPPERCASE_OFFSET

print(f"Sum of Priorities (Pt. 2): {sum_of_priorities}")