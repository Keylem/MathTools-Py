MainNumber = int(input("Çarpanlarına ayrılacak sayıyı alayım"))
bölücü = 2
çarpanları = list()
çarpantipi = list()
count = 0
finalstring = ""
while MainNumber != 1:
    if (MainNumber % bölücü) == 0:
        çarpanları.append(bölücü)
        MainNumber = MainNumber / bölücü
        print(bölücü)

        if not (bölücü in çarpantipi):
            çarpantipi.append(bölücü)
    else:
        bölücü += 1

print(çarpanları)
print(çarpantipi)

for x in çarpantipi:
    for y in çarpanları:
        if x == y:
            count += 1
    finalstring = finalstring + "{}^{}.".format(x,count)
    count = 0

finalstring = finalstring[0:(len(finalstring)-1)]
print(finalstring)


