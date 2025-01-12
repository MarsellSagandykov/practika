#переменные
n = int(input("число больше 1: "))

# Список
numbers = [True] * (n + 1)
# от 2 до корня
for i in range(2, int(n**0.5) + 1):
    if numbers[i]:
        for j in range(i * i, n + 1, i):
            numbers[j] = False

# Вывод
for num in range(2, n + 1):
    if numbers[num]:
        print(num)