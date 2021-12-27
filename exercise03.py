print('''💕 Welcome to My Guess Game Club 💕
You are here to guess the secret number
All the best for that...\n''')

secret_number = 18
totalGuesses = 9
tookGuesses = 0
while (True):
    
    print("You have",totalGuesses,"total guesses.")
    print("You took",tookGuesses,"guess.\n")

    guess_num = int(input("Enter your guess number: "))

    if guess_num > secret_number:
        print("guess shorter number to win.\n")

    elif guess_num < secret_number:
        print("guess higher number to win.\n")

    elif guess_num == secret_number:
        print("Congrats..👍,You guessed it right in",tookGuesses,"chances\n")
        break

    totalGuesses -=1
    tookGuesses += 1
    if tookGuesses == 9 and totalGuesses == 0:
        print("Sorry you used all your chances, now you dont have any, Game Over!...")
        break