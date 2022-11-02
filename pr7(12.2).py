def med(m, n, k):
    global a, b, c
    a = (2 * (n ** 2 + k ** 2) - m ** 2) ** 0.5 / 2
    b = (2 * (m ** 2 + k ** 2) - n ** 2) ** 0.5 / 2
    c = (2 * (m ** 2 + n ** 2) - k ** 2) ** 0.5 / 2


a, b, c = map(float, input().split())
if a < b + c and b < a + c and c < a + b:
    med(a, b, c)
    print(round(a, 2), round(b, 2), round(c, 2))
else:
    print('треугольник с такими сторонами не существует')
