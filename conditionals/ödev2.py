geosekil=(input("Hangi geometrik şekilden bahsediyorsunuz:"))
dortgen=("Dörtgen")
ucgen=("Üçgen")
if geosekil == dortgen :
    kenar1=int(input("1.kenarı giriniz:"))
    kenar2=int(input("2.kenarı giriniz:"))
    kenar3=int(input("3.kenarı giriniz:"))
    kenar4=int(input("4.kenarı giriniz:"))

    if (kenar1==kenar2) and (kenar2==kenar3) and (kenar3==kenar4) and (kenar4==kenar1):
        print("Bu bir kare")
    else: 
        print("Bu bir dörtgen")
elif geosekil == ucgen:
 kenar1=int(input("kenar1 giriniz:"))
 kenar2=int(input("Kenar2 giriniz:"))
 kenar3=int(input("kenar3 giriniz:"))
if (kenar1==kenar2) and (kenar2==kenar3):
  print("Bu bir eşkenar")


