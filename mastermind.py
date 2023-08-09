import random

num = random.randrange(1000, 10000)
print("The answer is: " + str(num))

while(1):
    n = int(input("Guess the 4 digit number:"))

    if n not in range(1000, 10000):
        print("Your guess is out of range")
        continue
    
    print("Your guess: " + str(n))

    if (n == num):
        print("Correct answer!")
        break
    else:
        print("Wrong answer!")
