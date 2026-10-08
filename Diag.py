with open("D:/Dwnlds/sequence.txt") as file:
    nums = [float(line.strip()) for line in file]

pos = 0
neg = 0

for num in nums:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

tot = pos + neg #если в файле нет нулей

green = "\033[42m"
red = "\033[41m"
reset = "\033[0m"

posproc = (pos / tot) * 100
negproc = (neg / tot) * 100

poswidth = round(posproc)
negwidth = round(negproc)

print(f"Положительных чисел: {pos}шт. - {posproc:.2f}%")
print(f"Отрицательных чисел: {neg}шт. - {negproc:.2f}%")

print(green + " " * poswidth + reset + red + " " * negwidth + reset)