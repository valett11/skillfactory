n = int(input('Введите число приобретаемых билетов: '))
l = [int(input("Введите возраст: ")) for x in range(1, n + 1)]
count_18_25 = 0
count_more_25 = 0

for i in l:
    if 18 <= i < 25:
        count_18_25 += 1
    if i >= 25:
        count_more_25 += 1
if n > 3:
    s = (count_18_25 * 990 + count_more_25 * 1390) * 0.9
    print('Вам полагается скидка 10%')
else:
    s = count_18_25 * 990 + count_more_25 * 1390
print("Общая стоимость билетов: ", s, " рублей")