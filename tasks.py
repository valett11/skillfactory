money = int(input('Укажите сумму под проценты: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for x in per_cent.values():
    deposit.append(x * money / 100)
print(deposit)
print('Максимальная сумма, которую вы можете заработать: ', max(deposit))
