from time import sleep

def countdown(seconds):
    while seconds > 0:
        print(f'{seconds} SECOND(S)!')
        seconds -= 1

    print('HAPPY NEW YEAR!')

def countdown_with_sleep(seconds):
    while seconds:
        print(f'{seconds} SECOND(S)!')
        seconds -= 1
        sleep(1)

    print('HAPPY NEW YEAR!')