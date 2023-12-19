list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

count = len(list_players)

team_one = list_players[:int(count/2)]
team_two = list_players[int(count/2):]

print(team_one)
print(team_two)
