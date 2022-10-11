vize1=float(input('1. vize notunu giriniz:'))
vize2=float(input('2.vize notunu giriniz:'))
final=float(input('final notunu giriniz:'))
ort=((vize1+vize2)/2* 0.6) + (final*0.4)

if (ort>= 90):
    print("Harf notunuz: AA")


elif (ort>=85):
    print("Harf notunuz: BA")

elif (ort>=80):
    print("Harf notunuz: BB")

elif (ort>=75):
    print("Harf notunuz: CB")

elif (ort>=70):
    print("Harf notunuz: CC")

elif (ort>=65):
    print("Harf notunuz: DC")

elif (ort>=60):
    print("Harf notunuz: DD")

elif (ort>=55):
    print("Harf notunuz: FD")

elif (ort<55):
    print("Seni okulda çok sevdik bu derste bir daha göremk istiyoruz bu yüzden :)")

print("Ortalaman={}".format(ort))


