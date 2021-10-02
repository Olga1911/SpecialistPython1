Моё решение:
from random import randint
list_numbers = []
n = int(input("n: "))
for item in range(0, n):
    list_numbers.append(randint(-100, 100))
print(list_numbers)
