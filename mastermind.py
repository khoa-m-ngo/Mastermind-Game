import random

# generate a random number from 1000-9999
num = random.randrange(1000, 10000)
print("The answer is: " + str(num))

while(1):
    n = input("Guess the 4 digit number: ")

    # if the input is not a number, end the game
    if not n.isdigit():
        break  

    # checking that the input is within range: 1000-9999
    if int(n) not in range(1000, 10000):
        print("Your guess is out of range")
        continue
    
    print("Your guess: " + n)

    # compare input against answer and print the result
    nMatch = len((set(str(num))).intersection(set(n)))

    if (int(n) == num):
        print("Correct answer!")
        break
    elif (nMatch == len(str(num))):
        print("Incorrect, all digits matched, but is in the wrong order")
    else:
        # if answer is incorrect, print the number of digits that matched the answer.
        print("Incorrect, only " + str(nMatch) + " digits matched.")

print("Game Finished.")
