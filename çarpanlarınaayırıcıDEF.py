def çarpanlarınaAyır(MainNumber):
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

    return finalstring[0:(len(finalstring)-1)]


print(çarpanlarınaAyır(55)) #Sayıyı giriniz
