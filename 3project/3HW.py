#ввод температуры
temp_input = input("Введите температуру, (БЕЗ ПРОБЕЛА): ")
    
#Value = Убираем последнее значение. unit = переводим последнее значение в верхний регистр
value = temp_input[:-1]
unit = temp_input[-1].upper()

#Проверка числа ли все, что не в конце
if not value.isdigit() and not (value[0] == '-' and value[1:].isdigit()):
    print("Ошибка, вы указали С или F вначале, а не в конце, а так нельзя!.")

#Строчку в число
value = int(value)

#C -> F
if unit == 'C':
    converted_temp = (value * 9 / 5) + 32
    print(f"{value}C -> {int(converted_temp)}F")

# F -> C
if unit == 'F':
    converted_temp = (value - 32) * 5 / 9
    print(f"{value}F -> {int(converted_temp)}C")