tickets = int(input('Укажите колличество билетов: '))
ages = []

for i in range(0,tickets):
    entered_value = int(input(f'Укажите возраст {i + 1} участника:\n'))
    ages.append(entered_value)

    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return  990
        else:
            return 1390

    full_price = sum(map(price, ages))

discount_price = int(full_price * 0.9)
if tickets > 3:
    print('Общая стоймость билетов со скидкой: ', discount_price, 'руб.')
else:
    print('Общая стоймость билетов: ', full_price, 'руб.')
