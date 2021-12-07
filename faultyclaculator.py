first_num = int(input("Enter the first number: "))
oprator = input("Enter the operator and i.e; +,-,x,/: ")
second_num = int(input("Enter the second number: "))

if first_num == 45 and oprator == 'x' and second_num == 3:
    print(555)

elif first_num == 56 and oprator == '+' and second_num == 9:
    print(77)

elif first_num == 56 and oprator == '/' and second_num == 6:
    print(4)

elif oprator == 'x':
    print(first_num * second_num)

elif oprator == '+':
    print(first_num + second_num)

elif oprator == '-':
    print(first_num - second_num)

elif oprator == '/':
    print(first_num/second_num)

else:
    print("Enter a valid operator.")