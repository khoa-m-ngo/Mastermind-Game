import random

# generate a random number from 100-999
answer = random.randrange(100, 1000)

# print("The answer is: " + str(answer)) #Debug code

print("Hello! In this game, you will guess a 3 digit passcode.")
print("For each incorrect try, you will be provided with a hint.")
print("Guess the passcode using the minimum number of tries.\n")

nTries = 0

start = "n"
while(start != "y"):
    start = input("Ready? (y/n): ")

while(1):
    n = input("\nGuess the 3 digit number: ")
    nTries += 1
    # if the input is not a four digits number, it is invalid
    if not n.isdigit() or len(n) != len(str(answer)):
        print("Must be a 3 digit number. Try again...")
        continue  
    
    print("Your guess: " + n)

    # compare input against answer and print the result
    nMatch = 0
    for i in range(0, len(n)):
        if (str(n)[i] == str(answer)[i]):
            nMatch += 1

    # nMatch = len((set(str(answer))).intersection(set(n)))

    if (int(n) == answer):
        print("Correct! Total number of tries: " + str(nTries))
        break
    elif (nMatch == 0):
        print("None of the digits matched.")
    else:
        # if answer is incorrect, print the number of digits that matched the answer.
        print("Only " + str(nMatch) + " digits matched.")

print("Game Finished.")
