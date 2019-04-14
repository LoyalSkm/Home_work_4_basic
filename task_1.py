
print('''   
            красный - огонь         белый - метал
            зедёный - дерево        синий - воздух
            желтый - земля
                    ''')
def chin_calen():
    YEAR = ["Обезьяны", "Петуха", "Собаки",
            "Свиньи", "Крысы", "Быка",
            "Тигра", "Кролика", "Дакона",
            "Змеи", "Лошади", "Овцаы"
            ]
    COLOR = ["Металическ", "Водян", "Деревянн", "Огненн", "Землян"]
    value = input("Введите интерисующие даты ерез запятую, в формате (123, 321): ")
    china_keys = value.split(", ")   #делим по запятой строку на список
    for i in china_keys:
        try:
            pozition = int(i)
            calc_col = (pozition % 10)
            calc_year = (pozition % 12)
            if calc_col in (0, 1): color_poz = 0
            if calc_col in (2, 3): color_poz = 1
            if calc_col in (4, 5): color_poz = 2
            if calc_col in (6, 7): color_poz = 3
            if calc_col in (8, 9): color_poz = 4
            if calc_year in (0, 2, 3, 4, 9, 10, 11):
                podj_poz = "ой"
            elif calc_year in (1, 5, 6) and color_poz == 1:
                podj_poz = "ого"
            else:
                podj_poz = "ого"
            china_value = ("Год " + str(COLOR[color_poz]) + podj_poz + " " + str(YEAR[calc_year]))
        except:
            china_value = "Не верная форма заполнения"
        res = {i: china_value}
        print(res)


chin_calen()
