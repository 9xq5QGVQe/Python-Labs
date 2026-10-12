import os
import time

black = "\033[40m"
white = "\033[107m"
reset = "\033[0m"

os.system('cls')


for h in range(4): #количество кадров в одной анимации
    pusto = ""
    for i in range(3):
        for j in range(3):
            color = black if (i + j + h) % 2 == 0 else white
            pusto += color + "  "
        pusto += reset + "\n"
    print("\033[H" + pusto)
    time.sleep(0.4) #задержка между кадрами
