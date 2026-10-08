black = "\033[40m"
white = "\033[107m"
reset = "\033[0m"

count = 3 #состоит из трех строчек и трех столбцов

for i in range(count):
    pusto = ""
    for j in range(count):
        color = black if (i + j) % 2 == 0 else white
        pusto += color + "  "
    print(pusto + reset)