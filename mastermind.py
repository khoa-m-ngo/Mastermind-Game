import random

# generate a random number from 1000-9999
answer = random.randrange(100, 1000)
print("The answer is: " + str(answer))

print("")
print("Hello! In this game, you will guess a 3 digit passcode.")
print("For each incorrect try, you will be provided with a hint.")
print("Try to guess the passcode using the minimum number of tries.")
print("")

nTries = 0

start = "n"
while(start != "y"):
    start = input("Are you ready to start? (y / n): ")

while(1):
    print("")
    n = input("Guess the 3 digit number: ")
    nTries += 1
    # if the input is not a four digits number, it is invalid
    if not n.isdigit() or len(n) != len(str(answer)):
        print("Your guess must be a 3 digit number. Try again...")
        continue  
    
    print("Your guess: " + n)

    # compare input against answer and print the result
    nMatch = len((set(str(answer))).intersection(set(n)))

    if (int(n) == answer):
        print("Correct answer! Total number of tries: " + str(nTries))
        break
    elif (nMatch == len(str(answer))):
        print("All digits matched, but is in the wrong order")
    elif (nMatch == 0):
        print("Incorrect, none of the digits matched.")
    else:
        # if answer is incorrect, print the number of digits that matched the answer.
        print("Incorrect, only " + str(nMatch) + " digits matched.")

print("Game Finished.")
