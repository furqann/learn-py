find_divisors = int(input("Find divisor: "))
divisor_list = []
for item in range(1, 101):
    if find_divisors % item == 0:
        divisor_list.append(item)
print(divisor_list)