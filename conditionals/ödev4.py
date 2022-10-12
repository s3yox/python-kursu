print('Hoşgeldiniz.Giriş yapınız!')
count = 0

# string koaycağım için ""
password = ""
username = ""

# 3 kere sorması için loopa alıyorum
while password!='ahsenhoca' and username!='ahsenhoca' and count < 3:
    
    username = input("Kullanıcı ismi giriniz: ")
    password = input("Şifre giriniz: ")

    if password=='ahsenhoca' and username=='ahsenhoca':
     #Eşleşirse break ediyorum.
     print('Giriş Başarılı.Hoşgeldiniz Ahsen Hanım.')
     break

    else:
        print('Giriş reddedildi.Tekrar deneyin')
        count+=1     #countu arttırıp loopa sokuyorum böylece 0 dan 3 'e gelince duruyor.
else:
    print("Hakkınız kalmadı")