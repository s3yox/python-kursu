sayi1=int(input("Sayıyı girin: "))

def is_prime(sayi1):
    for number in range (2, sayi1 + 1): 
        if number > 1: 

          for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
is_prime(sayi1)
#ÇALIŞTIRAMADIM



