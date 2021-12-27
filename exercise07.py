from pygame import mixer
from time import time
from datetime import datetime

def musicPlay(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        userInput = input("Enter the right command to stop the alaram otherwise it's keep going:\n").lower()
        if userInput == stopper:
            print("\nThank you sir, have a good day ahead.")
            mixer.music.stop()
            break

def logStatus(msg):
    with open('mylog.txt','a') as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    print("\n---------- Welcome to Healthy Programmer. ----------\n")

    userName = input("Enter your name Please:\n")
    print(f"Hello {userName}, i am your assistant remainder, Your todo list for today is:\n")
    todo = {'Drink Water': 'You have to drink water in every 20 minutes','Eye Exercsie':'You have to do eye exercise in every 30 minutes','Physical Exercise':'You have to do physical exercise in every 45 minutes'}
    for key,value in todo.items():
        print(key,'--',value)

    initWater = time()
    initEye = time()
    initExercise = time()

    WaterSec = 10
    EyeSec = 20
    ExerciseSec = 30

    while True:
        if time() - initWater > WaterSec:
            print("\n----- It's Drink Water time -----\n----- It's Drink Water time -----\n----- It's Drink Water time -----")
            musicPlay('water.mp3','drank')
            initWater = time()
            logStatus('Drink Water at:')

        elif time() - initEye > EyeSec:
            print("----- It's Eye Exercise time -----\n----- It's Eye Exercise time -----\n----- It's Eye Exercise time -----")
            musicPlay('eye.mp3','doneeye')
            initEye = time()
            logStatus('Eye exercise done at:')

        elif time() - initExercise > ExerciseSec:
            print("----- It's Physical Exercise time -----\n----- It's Physical Exercise time -----\n----- It's Physical Exercise time -----")
            musicPlay('Exercise.mp3','doneexe')
            initExercise = time()
            logStatus('Exercise done at:')