blue = '\033[44m'
white = '\033[47m'
red = '\033[41m'
reset = '\033[0m'

height = 10
width = 15

for _ in range(height):
    print(
        f"{blue}{' ' * width}"
        f"{white}{' ' * width}"
        f"{red}{' ' * width}"
        f"{reset}"
    )