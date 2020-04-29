print('введите размер массива (больше двух)')
a = []
n = int(input())
if n <= 2:
    print('Это же меньше двух')
else:
    print('А теперь элементы')
    for massive in range(n):
        a.append(int(input()))
a.sort()
print('Массив: ', a)
print('Два максимальных числа: ', a[-1], a[-2])
print(a)