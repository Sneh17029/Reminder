import time
from pygame import mixer
mixer.init()


def stop(s):
    f = input(f"Enter E{s}DONE when done: ")
    while f.upper() != f"E{s}DONE":
        f = input(f"Enter E{s}DONE when done: ")
    mixer.music.stop()
    return


def office(officetime):
    print(officetime)
    i = time.time()
    n = 3500
    time.sleep(2)
    while '09:00:00' <= officetime <= '17:00:00':
        officetime = time.strftime("%H:%M:%S")
        j = time.time()
        if (int(j-i)) % 900 == 0 and n != 0:
            mixer.music.load('Water.mp3')
            mixer.music.play()
            print(f"You have to drink {n} ml of water anyhow before 5:00 pm")
            m = int(input("Enter amount of water drank in \"ml\": "))
            stop("W")
            n = n-m
            if n == 0:
                print("All done with your target: ")
            else:
                print("Remaining= ", n)

        if (int(j-i)) % 1800 == 0:
            mixer.music.load('Eyes.mp3')
            mixer.music.play()
            stop("E")

        if (int(j-i)) % 2700 == 0:
            mixer.music.load('Physical.mp3')
            mixer.music.play()
            stop("P")


a = time.strftime("%H:%M:%S")
office(a)
mixer.quit()
