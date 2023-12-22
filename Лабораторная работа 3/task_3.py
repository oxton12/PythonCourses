# TODO  Напишите функцию count_letters

def count_letters(text):
    lowered_text = text.lower()
    letter_dict = {}

    for text_symbol in lowered_text:
        if text_symbol.isalpha():
            letter_dict[text_symbol] = letter_dict.get(text_symbol, 0) + 1
    return letter_dict


# TODO Напишите функцию calculate_frequency

def calculate_frequency(symbol_dict):
    letter_sum = sum(symbol_dict.values())
    for symbol, amount in symbol_dict.items():
        symbol_dict[symbol] = amount / letter_sum

    return symbol_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
count_dict = count_letters(main_str)
freq_dict = calculate_frequency(count_dict)

for letter, freq in freq_dict.items():
    print(f"{letter}: {freq:.2f}")
