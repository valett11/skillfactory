# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов.
# Программа должна работать следующим образом:
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на конференцию,
# то дополнительно получает 10% скидку на полную стоимость заказа.

n = int(input())
l = [int(input()) for x in range(1, n + 1)]
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