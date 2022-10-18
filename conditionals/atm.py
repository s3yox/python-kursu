from hashlib import algorithms_guaranteed
import time as t 

user_pin = 9864
user_balance = 10000
user_name = "Ahsen"
print("Hoşgeldiniz", user_name, end ="\n\n")

secim = 9

while (True):
    print("\t\t0. Cıkıs and kapat")
    print("\t\t1. Hesap Bilgisi")
    print("\t\t2. Para çek")
    print("\t\t3. Para ekle")
    print("\t\t4. Return Card")

    secim = int(input("İşlem seçiniz >>"))
    print("\n\n")

    if secim == 0:
        print("Çıkış yapılıyor.... ")
        t.sleep(2)
        print("Çıkış yapıldı.Teşekkürler! \n\n")
        break
    elif secim in (1,2,3,4):
        deneme_hakki = 3
        while(deneme_hakki!=0):
            giris_sifresi = int(input("Lütfen 4 haneli şifreyi giriniz >"))

            if giris_sifresi == user_pin
               print("Hesap bilgileri doğru!\n\n")

               if secim==1:
                print("Hesaptaki para yükleniyor.....")
                t.sleep(2)
                print("Ahsen Hanım şuanki toplam paranız:", user_balance, end="\n\n\n")
                break
            elif secim == 2:
                print("")
                