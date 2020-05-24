def köklüYazım(inputstring):
    whilestatemenet = True
    katmansayısı = 0
    #
    if inputstring[0] == "√":
        return inputstring
                                                                                #     √
    elif ("√" in inputstring) == True:
        while whilestatemenet == True:
            if inputstring[katmansayısı:katmansayısı + 1] != "√":
                katmansayısı += 1
            else:
                whilestatemenet = False
        katsayı = int(inputstring[:katmansayısı]) ** 2
        kök = int(inputstring[katmansayısı + 1 :])
        inputstring = katsayı * kök
        
    else:
        inputstring = int(inputstring) ** 2
    return "√{}".format(inputstring)

print(köklüYazım("5"))  # sayıyı girizi (köklü/köksüz)
