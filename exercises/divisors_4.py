find_divisors = int(input("Find divisors: "))

divisor_list = []
for item in range(1, find_divisors + 1):
    if find_divisors % item == 0:
        divisor_list.append(item)

print(divisor_list)
