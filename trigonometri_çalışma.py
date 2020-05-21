import random   #√

def soruseçici(kütüphane):
    import random
    res = soru, cevap = random.choice(list(kütüphane.items()))
    cevapinput = str(input("{} = ?  ".format(soru)))
    if cevapinput == cevap:
        print("gotcha!")
    else:
        print("Yanlış! Cevap {} olacaktı".format(cevap))

sıfır = {"sin0":"0", "cos0":"1", "tan0":"0", "cot0":"sonsuz"}
otuz = {"sin30":"1/2", "cos30":"√3/2", "tan30":"1/√3", "cot30":"√3"}
kırkbeş = {"sin45":"√2/2","cos45":"√2/2","tan45":"1","cot45":"1"}
altmış = {"sin60":"√3/2", "cos60":"1/2" ,"tan60":"√3", "cot60":"1/√3"}
doksan = {"sin90":"1","cos90":"0","tan90":"sonsuz","cot90":"0"}
kümeseçici = random.randint(1,5)
while True:
    

    if kümeseçici == 1:
        soruseçici(sıfır)
        kümeseçici = random.randint(1,5)
    if kümeseçici == 2:
        soruseçici(otuz)
        kümeseçici = random.randint(1,5)
    if kümeseçici == 3:
        soruseçici(kırkbeş)
        kümeseçici = random.randint(1,5)
    if kümeseçici == 4:
        soruseçici(altmış)
        kümeseçici = random.randint(1,5)
    if kümeseçici == 5:
        kümeseçici(doksan)
        kümeseçici = random.randint(1,5)