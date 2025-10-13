start = int(input())
end = int(input())
n = int(input())
for i in range(start, end + 1):
    if i == n:
        print(f"!{n}!", end=" ")
    else:
        print(i, end=" ")