
import copy

sayi = 1000
sayikopya = 1000
for x in range(1,9999): 
    
    sayi = sayi + 1
    sayikopya = sayikopya + 1
    ters = 0    
    while(sayi > 0):    
        gecici = sayi %10    
        ters = (ters *10) + gecici    
        sayi = sayi //10    
     
    #print("\n Sayının Ters Çevrilmiş Hali = %d" %ters)
    #print(sayikopya*4)
    sayi = sayikopya

    if (sayikopya*4) == (ters):
        print(sayikopya)
