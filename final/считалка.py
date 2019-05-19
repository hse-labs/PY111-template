persons = ["чел01", "чел02", "чел03", "чел04", "чел05"]

print("\n", "правильная последовательность: ", "чел03", "чел02", "чел05", "чел04", "чел01", "\n")
print(persons)
kick = 0
start = 0


while len(persons) != 1:

    slog = 8
    kick = 8 % len(persons) - 1 + start
    start = kick
    print(persons[kick], "\n")
    persons.pop(kick)
    print(persons)