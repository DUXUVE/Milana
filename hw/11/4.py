def occurs_once(lst, n):
    count = 0
    for num in lst:
        if num == n:
            count += 1
    return count == 1

numbers = [1, 2, 3, 4, 3, 5]
target = 2
print(occurs_once(numbers, target))