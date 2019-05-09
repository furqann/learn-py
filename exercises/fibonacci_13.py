#  https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
def fib(num):
  if num == 1:
    return 1
  elif num == 0:
    return 0
  return fib(num - 1) + fib(num - 2)


print(fib(1))
print(fib(10))
