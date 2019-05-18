persons = ["чел01", "чел02", "чел03", "чел04", "чел05"]


# start = 2
# slog = 8
print(persons)
while len(persons) != 1:
    kick = 0
    start = kick
    slog = 8
    a = (len(persons) - start)
    if a > 8:
        a = (len(persons) - start) % len(persons)
    kick = 8 - a - 1
    if kick > len(persons):
        kick = kick % len(persons)
    print(persons[kick])
    persons.pop(kick)
    print(persons)