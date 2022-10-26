def ebob_bul(sayi1,sayi2):
    if(sayi1>sayi2):
        i=sayi2
    else:
        i=sayi1

    while(i>0):
        if(sayi1%i == 0 and sayi2%i==0):
            return i
        i-=1
    return 1
sayi1=int(input("ilk sayıyı girin: "))
sayi2=int(input("ikinci sayıyı girin: "))
print("ebob =",ebob_bul(sayi1,sayi2))   
#4          