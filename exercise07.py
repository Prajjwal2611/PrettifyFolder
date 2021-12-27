# import pyttsx3
# obj = pyttsx3.init()
# obj.say("Welcome to python programming. I am prajjwal, and i am learning python, and want to become a coder.")
# obj.save_to_file(obj.say'sample.mp3')
# obj.runAndWait()
       

# from datetime import datetime
# from pygame import mixer
# from time import time

# def musicPlay(file,stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play(-1)
#     while True:
#         a = input("Enter the right key to stop the alarm: ")
#         if a == stopper:
#             mixer.music.stop()
#             break

# def log_Status(msg):
#     with open('mylog.txt','a') as f:
#         f.write(f"{msg} {datetime.now()}\n")

# if __name__ == '__main__':
#     print("\n---------- Welcome to Programmer's Health Care ----------\n")
    
#     init_water = time()
#     init_eye = time()
#     init_exercise = time()

#     watersec = 40*60
#     eyesec = 30*60
#     exercisesec = 45*60

#     while True:
#         if time() - init_water > watersec:
#             print('''\n----- Drink Water time -----
# ----- Drink Water time -----
# ----- Drink Water time -----\n''')
#             musicPlay('water.mp3','drank')
#             init_water = time()
#             log_Status('Drink Water at: ')

#         elif time() - init_eye > eyesec:
#             print('''\n----- Eye Exercise time -----
# ----- Eye Exercise time -----
# ----- Eye Exercise time -----\n''')
#             musicPlay('eye.mp3','doneeye')
#             init_eye = time()
#             log_Status('Eye Exercise at: ')

#         elif time() - init_exercise > exercisesec:
#             print('''\n----- Exercise time -----
# ----- Exercise time -----
# ----- Exercise time -----\n''')
#             musicPlay('Exercise.mp3','doneexe')
#             init_exercise = time()
#             log_Status('Exercise done at: ')

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