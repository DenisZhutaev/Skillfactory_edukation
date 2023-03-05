'''Ввод клиентом банка суммы под процент'''
money = int(input('Введите сумму под процент: '))

'''Процентная ставка по банкам'''
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

'''Просчитываем накопленные средства за год'''
# Вариант решения № 1
savings = [int(i * money / 100) for i in per_cent.values()]
# print(*savings)

# Вариант решения № 2
# for bank, percent in per_cent.items():
#     summ_percent = int(percent * money / 100)
#     print(bank, summ_percent, end=', ')

# Вариант решения № 3
summ_percent = []
for bank, percent in per_cent.items():
    summ_percent.append(f'{bank} - {int(percent * money / 100)}')
print('\nНакопленные средства за год:')
print('\n'.join(summ_percent))  # красивый и понятный вывод для клиента

'''Вывод на экран максимального значения'''
print('\nМаксимальная сумма, которую вы можете заработать: {}'.format(max(savings)))
