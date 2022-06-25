

while True:
    user_input = int(input("Introduceti nr coloanei:"))
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

    if user_input == 1:
        sum1 = numbers[0]
        i = 1
        print(i,"-->",sum1)
    elif user_input == 2:
        sum2 = numbers[1] + numbers[2]
        i = 2
        print(i,"-->",sum2)
    elif user_input == 3:
        sum3 = numbers[3] + numbers[4] + numbers[5]
        i = 3
        print(i,"-->",sum3)
    elif user_input == 4:
        sum4 = numbers[6] + numbers[7] + numbers[8] + numbers[9]
        i = 4
        print(i,"-->",sum4)
    elif user_input == 5:
        sum5 = numbers[10] + numbers[11] + numbers[12] + numbers[13] + numbers[14]
        i = 5
        print(i,"-->",sum5)
        break