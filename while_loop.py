#  Loops
#  while
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

secret_number = 3
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry! you failed")