import time
#Ustawienia
plik = input()

#Wczytywanie informacji
plik_in = open("C:/Users/SzymonPC/Dysk Google/dokumenty/inne/des/in/" + plik + ".in")
ilosc_desek = plik_in.readline()
wymiary_desek = plik_in.readline()
plik_in.close()

#Zmienne i tablice
czas1 = time.time()
deskis = []
deskis = wymiary_desek.split()
licznik = 0
deski_duza = []
deski_sort = []
deski2_sort = []
deski_sort_cal = []
l_pustych = 0
najw = 0
ost = 0
b_czasy = []

#Zmiana typu tablicy
while licznik != len(deskis):
        deski_duza.append(int(deskis[licznik]))
        licznik += 1

################### DESKI 1
#Zerowanie i deklarowanie
#Sprawdzanie czy liość desek jest wystaczająca
if len(deski_duza) < 4:
        x = "0"
        print("0")
else:
        licz = 0
        licznik = 0
        licznik2 = 0

#        print(deski_duza)
        #deski_duza = [6, 3, 7, 6, 5, 8]
        for u in range(4):
                while 1 == 1:
                        if deski_duza[ost] > deski_duza[najw]:
                                najw = ost
                        ost += 1
                        if ost == len(deski_duza):
                                break
                deski_sort.append(deski_duza[najw])
                
                del deski_duza[najw]
#                deski_duza[najw] = 0

                najw = 0
                ost = 0
#        print("po sort:")                
#        print(deski_sort)

        #Wypisywanie największej możliwej do zbudowania piaskownicy
        print(deski_sort[3] ** 2)
        x = str(deski_sort[3] ** 2)

#Sprawdzanie czy wynik się zgadza
czas2 = time.time()
plik_out = open("C:/Users/SzymonPC/Dysk Google/dokumenty/inne/des/out/" + plik + ".out")
info = plik_out.readline()
info = info[:info.index("\n")]

if x == info:
        print("Dobrze!!!!!!!!!!!")
        print("czas: " + str(czas2 - czas1) + "s")
plik_out.close()
