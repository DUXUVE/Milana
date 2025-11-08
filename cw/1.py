count = int(input("В диапазоне от: "))
end = int(input("До: "))
multipues_sum = 0
count_multipues = 0
evens_sum = 0
count_evens = 0
odds_sum = 0
while count <= end:
    if count % 9 == 0:
        multipues_sum += count
    if count % 2 == 0:
        evens_sum += count
    else:
        odds_sum += count
    count += 1
print(multipues_sum)
print(evens_sum)
print(odds_sum)