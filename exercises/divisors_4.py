#  https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
find_divisors = int(input("Find divisors: "))
check_upto = find_divisors + 1
divisor_list = [divisor for divisor in range(1, check_upto) if find_divisors % divisor == 0]
print(divisor_list)
