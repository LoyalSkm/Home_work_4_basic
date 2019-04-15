def pow_list():
    value = input("Введите данные в фотмате: (14,2),(-16,0.5),(12, True#Error#)")
    start_list = value.replace(" ", "").replace("),(", "), (").split(", ") # Список из отдельных елементовсодержащих 2 числа
    def prov(mes):
        while True:
            try:
                val = float(mes)
                return True
            except:
                return False
    for i in start_list:
        cau_list = i.replace("(","").replace(")", "").split(",") # Отделяю 2 числа от лишних скобок и запятых
        try:

            prov_a = prov(cau_list[0])
            prov_b = prov(cau_list[1])
            if prov_a and prov_b == True:
                res = float(cau_list[0]) ** float(cau_list[1])
            elif prov_a == True and prov_b == False:
                res = "Сомножитель задан не корректно"
            elif prov_a == False and prov_b == True:
                res = "Множитель задан не корректно"
            elif prov_a == False and prov_b == False:
                res = " И множетель и сомножитель заданны не корректно"
            print(i + ": {} ** {} = {}".format(cau_list[0], cau_list[1], res))
        except IndexError:
            res = "Задан только множитель или пустая ячейка"
            print(i + ":{} = {}".format(cau_list[0], res))
pow_list()

