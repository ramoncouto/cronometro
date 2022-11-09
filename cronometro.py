from time import sleep
from os import system
time = [[], [], []]
insert_hour = int(input('Horas: '))
time[0].append(insert_hour)
insert_minute = int(input('Minutos: '))
time[1].append(insert_minute)
insert_second = int(input('Segundos: '))
time[2].append(insert_second)
if time[0][0] > 0:
    for hour in range(time[0][0], -1, -1):
        for minute in range(time[1][0], -1, -1):
            if minute == 0 and hour > 0:
                time[1].pop()
                time[1].append(59)
            for second in range(time[2][0], -1, -1):
                if second == 0 and minute > 0:
                    time[2].pop()
                    time[2].append(59)
                print(f'{hour} : {minute} : {second}')
                sleep(1)
                system('cls')
else:
    if time[1][0] > 0:
        for minute in range(time[1][0], -1, -1):
            for second in range(time[2][0], -1, -1):
                if second == 0 and minute > 0:
                    time[2].pop()
                    time[2].append(59)
                print(f'{minute} : {second}')
                sleep(1)
                system('cls')
    else:
        for second in range(time[2][0], -1, -1):
            print(f'0 : {second}')
            sleep(1)
            system('cls')
