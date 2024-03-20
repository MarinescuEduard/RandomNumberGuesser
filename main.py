from random import randrange
insertedNumber = randrange(1, 10)
numberOfTries = int(0)
condition = 1
print("Insert a number smaller or equal to 10:")
guessedNumber = int(input())
while condition != 1:
    while guessedNumber >= 10:
        print("The number is bigger than 10:")
        guessedNumber = int(input())
    if guessedNumber < 10:
        numberOfTries += 1
        if guessedNumber == insertedNumber:
            print("Congratulation!")
            break
        if numberOfTries == 3:
            print("Too bad you reached the maximum tries. The number was  ", insertedNumber)
            break
        if abs(guessedNumber - insertedNumber) >= 3:
            print("Wrong value! It's cold.")
            guessedNumber = int(input())
        elif abs(guessedNumber - insertedNumber) < 3:
            print("Wrong value! It's hot.")
            guessedNumber = int(input())
