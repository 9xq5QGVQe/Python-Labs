func = "     y\n"
sootnoshenie = 32

for i in range(32, -1, -1):
    y = i / 2
    pos = round(y ** 0.5 * 8) #количество пробелов между числами на оси x
    if i % 4 == 0:
        func += f"{y:4.0f} |"
    else:
        func += "     |"
    func += " " * pos
    func += "*" * (sootnoshenie - pos + 1)
    func += "\n"

    sootnoshenie = pos

func += "     +" + "-" * 33 + "> x\n"
func += "       0       1       2       3       4"
print(func)
