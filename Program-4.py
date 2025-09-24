numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

result = {}

for d in range(1, 10):   # from 1 to 9
    count = 0
    for num in numbers:
        if num % d == 0:   # check divisibility
            count += 1
    result[d] = count

print(result)