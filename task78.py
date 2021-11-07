xlist = ["Х-Фактор","Звезды сошлись","Калыханка","Мужское/Женское"]
for y in xlist:
    print(y)
z = input("Введите свою передачу: ")
x = int(input("Выберите позицию: "))
xlist.insert(x,z)
for y in xlist:
    print(y)