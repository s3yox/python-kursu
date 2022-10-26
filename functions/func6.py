def alan_hesaplama(name):
    if name == "dikdörtgen":
        ken1 = int(input("Kenar1 uzunluğu giriniz: "))
        ken2 = int(input("Kenar2 uzunluğu giriniz: "))
        dikd_alan = ken1*ken2
        print(f"Dikdörtgenin alanı = {dikd_alan}")
    elif name == "kare":
        kenar = int(input("Karenin bir kenarını girin"))
        kare_alan= kenar*kenar 
        print(f"Karenin alanı = {kare_alan}")
    elif name == "çember":
        ycap=int(input("Çemberin yarıçapı: "))
        pi=3.14
        cember_alan= pi*ycap*ycap
        print(f"Çemberin alanı = {cember_alan}")
    elif name == "üçgen":
        taban=int(input("Üçgenin taban uzunluğu: "))
        yukseklik=int(input("Üçgenin yüksekliği: "))
        ucgen_alan=0.5*taban*yukseklik
        print(f"Üçgenin alanı = {ucgen_alan}")
    else:
        print("Bu şekil opsiyonalrımızda yoktur.") 


print("Alanı hesaplanabilen şekiller: ")
print("Kare ")
print("Dikdörtgen")
print("Üçgen")
print("Çember")
name=input("Hesaplamak iste4diğiniz şeklin ismi: ")
name= name.lower()
alan_hesaplama(name)


    