Мое решение: 
a = int(input("a: "))
length = "#"
width = " "
if 2 < a <= 30:
    print(length * a)
    print(((length + width * (a - 2) + length) + "\n") * (a - 2), end="")
    print(length * a)
