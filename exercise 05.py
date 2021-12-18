client_list = {1:'Prajjwal', 2:'Priyana', 3:'bhai', 4:'lala bhai'}
log_list = {1:'Diet', 2:'Exercise'}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Here is the list of clients:\n")
    for key,value in client_list.items():
        print('Press',key,'For',value,'\n',end='')
    list_key = int(input("\nEnter the correct key for futher updates: "))

    print("\nPress 1 for log")
    print("Press 2 for retrieve\n")
    op = int(input("Enter the correct key: \n"))

    if op == 1:
        for key,value in log_list.items():
            print('Press',key,'for',value,'\n',end='')
        log_name = int(input('\nEnter the correct key to step forward: '))
        print("Selected: ",log_list[log_name])
        f = open(client_list[list_key]+"_"+log_list[log_name]+".txt","a")
        k = 'y'
        while k != 'n':
            print("\nEnter your",log_list[log_name],': ')
            log_input = input()
            f.write('['+str(getdate())+']'+log_input+'\n')
            k = input('Do you want to add more y(yes),n(no): ')
            continue
        f.close()

    elif op == 2:
        for key,value in log_list.items():
            print('Press',key,'for',value,'\n',end='')
        log_Name = int(input('Enter the right key to step forward: '))
        print(client_list[list_key],'-',log_list[log_Name],'Report:\n')
        f = open(client_list[list_key]+"_"+log_list[log_Name]+'.txt')
        input1 = f.readlines()
        for i in input1:
            print(i,end="")
        f.close()

    else:
        print("Invalid input!..")

except Exception as e:
    print("Wrong input!..")
