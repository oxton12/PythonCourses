money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

count = 0
current_money = money_capital

while True:
    current_money -= spend - salary
    if current_money < 0:
        break
    count += 1
    spend += spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", count)
