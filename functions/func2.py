def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

print('Hoşgeldiniz.Lütfen yapacağınız işlemi seçiniz!')
print('1.Toplama')
print('2.Çıkarma')
print('3.Çarpma')
print('4.Bölme')

secim=int(input('Seçiminizi giriniz: '))

num1=int(input('1.sayıyı giriniz: '))
num2=int(input('2.sayıyı griniz:'))

if secim == 1:
    print("İşleminizin sonucu= ",add(num1,num2))
elif secim == 2:
    print("İşleminizin sonucu= ",substract(num1,num2))
elif secim == 3:
    print("İşleminizin sonucu= ",multiply(num1,num2))
elif secim == 4:
    print("İşleminizin sonucu= ",divide(num1,num2))
else:
    print("Böyle bir işlem seçeneği yoktur.")