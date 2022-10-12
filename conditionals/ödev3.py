
sayi = int(input("Sayıyı Giriniz: "))
toplam = 0
gecici = sayi
while gecici > 0:
   digit = gecici % 10
   toplam += digit ** 3
   gecici //= 10


if sayi == toplam:
   print(sayi,"bir armstrong sayıdır")
else:
   print(sayi,"armstrong sayı değildir")
