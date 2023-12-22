# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, sep=","):
    group1_listed = group1.split(sep)
    group2_listed = group2.split(sep)
    intersection = list(set(group1_listed).intersection(group2_listed))
    intersection.sort()
    return intersection


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))
