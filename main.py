spis=input("Введите строку для определения(на русском!!!):")
#инициализация данных
gls = 0
sgl = 0
length = 0
vse_gls="аяуюоеёэиыАЯУЮОЕЁЭИЫ"
vse_sgl="бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФЧЦЧШЩ"
for char in spis:
    length += 1
    if char in vse_gls:
        gls += 1
    elif char in vse_sgl:
        sgl += 1

print('Количество гласных',gls)
print('Количество согласных',sgl)
print('Количество укв в строке',length)