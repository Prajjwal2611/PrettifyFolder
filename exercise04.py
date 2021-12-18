# Pattern Program for odd input and even input.
try:
    inputRows = int(input("Enter the number of rows: "))
    inputBoolean = int(input("Enter 1 for star pattern and 0 for reverse star pattern: "))
    newBoolInput = bool(inputBoolean)
    if newBoolInput == True:
        for i in range(inputRows):
            for j in range(i+1):
                print('*', end=" ")
            print()
    elif newBoolInput == False:
        for i in range(inputRows,0,-1):
            for j in range(i):
                print("*", end=" ")
            print()
except Exception as e:
    print(e)