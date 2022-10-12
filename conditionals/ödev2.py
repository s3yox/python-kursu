geosekil=(input("Hangi geometrik şekilden bahsediyorsunuz:"))
dortgen=("Dörtgen")
ucgen=("Üçgen")
if geosekil == dortgen :
    a=int(input("1.kenarı giriniz:"))
    b=int(input("2.kenarı giriniz:"))
    c=int(input("3.kenarı giriniz:"))
    d=int(input("4.kenarı giriniz:"))

    if (a==b) and (b==c) and (c==d) and (d==a):
        print("Bu bir kare")
    else: 
        print("Bu bir dörtgen")
elif geosekil == ucgen:
 a=int(input("a giriniz:"))
 b=int(input("b giriniz:"))
 c=int(input("c giriniz:"))
 if (a==b) and (b==c):
   print("Bu bir eşkenar")
 elif (a==b) and (a!=c):
     print("Bu ikizkenar")