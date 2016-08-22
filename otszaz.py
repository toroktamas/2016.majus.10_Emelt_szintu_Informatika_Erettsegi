#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""2016.majus.10 Emelt szintu Informatika erettsegi megoldas python programozasi nyelven."""
def ertek(mennyiseg):
    if mennyiseg == 1:
        vissza = 500
    elif mennyiseg == 2:
        vissza = 500+450
    elif mennyiseg == 3:
        vissza = 500+450+400
    elif mennyiseg > 3:
        vissza = 500+450+400+((mennyiseg-3)*400)
    
    return vissza

#print("1. feladat")
"""Be kell olvasni a penztar.txt allomanyt amit en egy szotarba gondoltam megtenni.Ami igy nezne ki:
fizetes={
    "Hanyadik":[vasarolt dolgok]
}
"""
fizetes={}
n=1
sz=0
with open("penztar.txt","rt",encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n","")
        sz+=1
        if sz == 1:
            fizetes[n]=[]
            fizetes[n].append(sor)
            continue
        if sor == "F":
            n+=1
            fizetes[n]=[]
        else:
            fizetes[n].append(sor)
print(fizetes)

print("2. feladat")
"""Meg kell hatarozni hogy hanyszor fizzettek a penztarnal."""
print("A fizetesek szama: {}\n".format(len(fizetes)-1))

print("3. feladat")
"""Ki kell irni hogy az elso vasarlonak hany arucikk volt a kosaraban."""
print("Az elso vasalo {} darab arucikket vasarolt.\n".format(len(fizetes[1])))

print("4. feladat")
"""Be kell kerni egy vasarlas sorszamat egy arucikk nevet es egy mennyiseget."""
sorszam = int(input("Adja meg egy vasarlas sorszamat! "))
arucikk = str(input("Adja meg egy arucikk nevet! "))
mennyiseg = int(input("Adja meg a vasarolt darabszamot! "))
print("\n")

print("5. feladat")
"""Meg kell hatarozni hogy a bekert aruzikkbol mikor vettek eloszor es mikor utoljara es hogy hanyszor vettek."""
listam=[]
for k,v in fizetes.items():
    if arucikk in v:
        listam.append(k)
print("Az elso vasarlas sorszama: {}".format(sorted(listam)[0]))
print("Az utolso vasarlas sorszama: {}".format(sorted(listam)[-1]))
print("{} alkalommal vasaroltak belole.\n".format(len(listam)))

print("6. feladat")
"""Hatarozza meg hogy ha bekert darabszamot vasaroljuk az adott termekbol akkor mennyit kell fizetni?"""
print("{0} darab vetelekor fizetendo: {1} \n".format(mennyiseg, ertek(mennyiseg)))

print("7. feladat")
"""Meg kell hatarozni hogy a bekert vasarlas sorszamakor melyik arucikkbol hanyat vasaroltak."""
for x in set(fizetes[sorszam]):
    print(str(fizetes[sorszam].count(x))+" "+x)   

#print("8. feladat")
"""osszeg.txt fajt el kell kesziteni soronkent a vasarlas mintajanak megfeleloen egy vasarlas keruljon ehez csinalok egy fuggvenyt."""
def ar(termek):
    """ vasarolt - vasarolt termekek szama """
    teljes_ar = 0
    for k in set(termek):
        hany = termek.count(k)
        if hany == 1:
            fizetendo = 500
        elif hany == 2:
            fizetendo = 500+450
        elif hany == 3:
            fizetendo = 500+450+400
        elif hany > 3:
            fizetendo = 500+450+400+((hany-3)*400)

        teljes_ar += fizetendo
    
    return teljes_ar

with open("osszeg.txt", "wt", encoding="utf-8") as g:
    for k,v in fizetes.items():
        g.write("{0}: {1}\n".format(k, ar(v)))
