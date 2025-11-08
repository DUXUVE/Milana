def squares(lst):
    result = []
    for num in lst:
        result.append(num * num)
    return result

numbers = [1, 2, 3, 4, 5]
print(squares(numbers))