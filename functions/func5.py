import time as t
user_name= "Ahsen"
user_password= 18811923
user_ninput=input("Kullanıcı adını giriniz: ")
user_passinput=int(input("Şifre griniz:"))
bakiye= 3569
miktar=0
yenibakiye=0
def paraEkle(miktar):
    miktar=int(input("Ne kadar eklemek istiyorsunuz?: "))
    yenibakiye=bakiye+miktar
    print(f'Bakiyenize {miktar} kadar tl eklendi.Paranız {yenibakiye} tl oldu ')
    return yenibakiye
def paraCek(miktar):
    miktar=int(input("Ne kadar çekmek istiyorsunuz?: "))
    yenibakiye=bakiye-miktar
    if yenibakiye<0:
        print("Bu işlem gerçekleşemez.")
    else:
        print(f'Bakiyenize {miktar} kadar tl çekildi.Paranız {yenibakiye} tl oldu ')


if (user_name==user_ninput and user_password==user_passinput):
        print("Hesap bilgileri doğrulandı.Sisteme aktarılıyorsunuz....")
        t.sleep(2)
        print("İşlem seçiniz....")
        print("1.Bakiye Görüntüle...")
        print("2.Para Ekle...")
        print("3.Para Çek...")
        secim=int(input("Seçtiğiniz işlemi tuşlayınız: "))
        if secim == 1:
            print("Lütfen bekleyin....")
            t.sleep(2)
            print(bakiye)
        if secim == 2:
            print("Lütfen bekleyin....")
            t.sleep(2)
            paraEkle(miktar)
        if secim== 3:
            print("Lütfen bekleyin....")
            t.sleep(2)
            paraCek(miktar)
else:
    print("kullanıcı bilgileri hatalı polis aranıyor ve hesap sahibi bilgilendiriliyor.")
            
        
        
        