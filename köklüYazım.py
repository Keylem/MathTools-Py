inputstring = str(input("sayıyı alayım (köklü/köksüz)"))
whilestatemenet = True
katmansayısı = 0
#                                                                            #     √
if ("√" in inputstring) == True:
    while whilestatemenet == True:
        if inputstring[katmansayısı:katmansayısı + 1] != "√":
            katmansayısı += 1
        else:
            whilestatemenet = False
    katsayı = float(inputstring[:katmansayısı]) ** 2
    kök = float(inputstring[katmansayısı + 1 :])
    inputstring = katsayı * kök
    
else:
    inputstring = int(inputstring) ** 2

print("√{}".format(inputstring))