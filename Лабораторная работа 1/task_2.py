# TODO Найдите количество книг, которое можно разместить на дискете

space_in_Mb = 1.44
pages = 100
lines_on_page = 50
symbols_in_line = 25
symbol_weight = 4

one_book_weight = pages * lines_on_page * symbols_in_line * symbol_weight
space_in_bites = int(1.44*1024**2)

print("Количество книг, помещающихся на дискету:", round(space_in_bites/one_book_weight))
