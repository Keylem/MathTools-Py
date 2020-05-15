import random

classs = [*range(1,22)]
f = str(input("y?"))

while True:
    if f == "y":
        print(classs.pop(random.randrange(0,len(classs))))
        k = str(input("continuez..."))
        if len(classs) == 0:
            print("Tout le monde a participé au cours!")
            exit()