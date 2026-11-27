from nim import train, play

numTrain = 0
invalid = True
while invalid:
    difficulty = int(input("Pick your difficulty: 1. Easy, 2. Medium, 3. Hard (input a number): "))
    if difficulty == 1:
        invalid = False
        numTrain = 1000
    elif difficulty == 2:
        invalid = False
        numTrain = 10000
    elif difficulty == 3:
        invalid = False
        numTrain = 100000
    else:
        print("Invalid.")
ai = train(numTrain)
play(ai)
