def tamBolenleribul(sayi):
    tambolenler = []
    for i in range(2,sayi):
        if (sayi % i == 0):
            tambolenler.append(i)

    return tambolenler

print(tamBolenleribul(20))