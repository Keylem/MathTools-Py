def köklüYazımToplayıcı(inputstring):
    if inputstring.startswith("√"):
        inputstring = "1" + inputstring

    def kökdışı(inputstring):
        inputlist = inputstring.split(".")

        inputlist2 = [x.split("^") for x in inputlist]
        inputlist3 = list()

        for y in inputlist2:
            if y != [""]:
                asılsayı = int(y[0])
                katsayı = int(y[1])
                üssüiki = katsayı // 2
                kökkalanı = katsayı % 2

                listeiçi = [asılsayı, üssüiki, kökkalanı]
                inputlist3.append(listeiçi)

        return inputlist3

    whilestatemenet = True
    katmansayısı = 0

    if inputstring.startswith("√") == True:

        inputstring = inputstring[1:]
        #     √
    elif ("√" in inputstring) == True:
        while whilestatemenet == True:
            if inputstring[katmansayısı:katmansayısı + 1] != "√":
                katmansayısı += 1
            else:
                whilestatemenet = False
        katsayı = float(inputstring[:katmansayısı]) ** 2
        kök = float(inputstring[katmansayısı + 1:])
        inputstring = katsayı * kök

    else:
        inputstring = int(inputstring) ** 2

    MainNumber = inputstring
    bölücü = 2
    çarpanları = list()
    çarpantipi = list()
    count = 0
    finalstring = ""
    while MainNumber != 1:
        if (MainNumber % bölücü) == 0:
            çarpanları.append(bölücü)
            MainNumber = MainNumber / bölücü

            if not (bölücü in çarpantipi):
                çarpantipi.append(bölücü)
        else:
            bölücü += 1

    for x in çarpantipi:
        for y in çarpanları:
            if x == y:
                count += 1
        finalstring = finalstring + "{}^{}.".format(x, count)
        count = 0
    rawçarpım = 1
    rawkök = 1
    for f in kökdışı(finalstring):
        katsayı = f[0]
        kökdışıdeğeri = f[1]
        kökiçideğeri = f[2]

        if katsayı * kökdışıdeğeri != 0:
            rawçarpım = katsayı ** kökdışıdeğeri * rawçarpım  
        if katsayı * kökiçideğeri != 0:
            rawkök = rawkök * katsayı * kökiçideğeri
    if rawkök == 1:
        return("{}".format(rawçarpım))
    else:
        return ("{}√{}".format(rawçarpım, rawkök))


# print(köklüYazımToplayıcı("5555555√888")) #içerideki sayı 2147483648'dan büyük OLAMAZ!

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
        kök = int(inputstring[katmansayısı + 1:])
        inputstring = katsayı * kök

    else:
        inputstring = int(inputstring) ** 2
    return "√{}".format(inputstring)


def sonuçprint(kırkbeş, doksan):
    print("Kırkbeş derecenin karşısı = {}".format(kırkbeş))
    print("kırkbeş derecenin karşısı = {}".format(kırkbeş))
    print("doksan derecenin karşısı = {}".format(doksan))


soru = int(input("45-90?"))
kenardeğeri = str(input("Açıya denk gelen kenarın değerini giriniz"))

if (soru == 45):
    kırkbeş = köklüYazımToplayıcı(kenardeğeri)
    doksan = köklüYazımToplayıcı("√" + str(int(köklüYazım(kenardeğeri)[1:]) * 2))

if (soru == 90):
    if int(köklüYazım(kenardeğeri)[1:]) % 2 == 0:
        kırkbeş = köklüYazımToplayıcı("√" + str(int(köklüYazım(kenardeğeri)[1:]) // 2))
        doksan = köklüYazımToplayıcı(kenardeğeri)
    
    else:
        kırkbeş = "(" + köklüYazımToplayıcı("√" + str(int(köklüYazım(kenardeğeri)[1:]) * 2)) + ")/2"
        doksan = köklüYazımToplayıcı(kenardeğeri) 




sonuçprint(kırkbeş, doksan)
