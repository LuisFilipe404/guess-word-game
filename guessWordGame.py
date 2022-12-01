import random

playerName = input("Enter your name: ")
print("Good Lucky", playerName, "!\n")

dictWords = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

guessThisWord = random.choice(dictWords)

guessedWords = ''

turns = 12

while turns > 0:
    
    victoryCondition = 0

    for char in guessThisWord:
        if char in guessedWords:
            print(char)
        else: 
            print("_")
            victoryCondition += 1
    

    if victoryCondition == 0:
        print("\nYou have won!")
        print("The word is:", guessThisWord)
        break

    yourGuess = input("\nGuess a character: ")
    
    guessedWords += yourGuess
    

    turns -= 1

    print("You have", turns, "turns")

if turns == 0:
    print("\nYou not gessed a word, try again!")
    print("The word was", guessThisWord)
    
print("\nFinished Algorithm")