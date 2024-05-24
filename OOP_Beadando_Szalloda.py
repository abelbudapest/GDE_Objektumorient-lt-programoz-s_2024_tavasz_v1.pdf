import datetime
import uuid
import random
#from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar=ar
        self.szobaszam=szobaszam
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, foglalt, foglDatum, vendegNeve, ar=300, agyszam=1):
        super().__init__(ar, szobaszam)
        self.agyszam=1
        self.foglalt=False
        self.foglDatum=foglDatum
        self.vendegNeve=vendegNeve
    pass

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, foglalt, foglDatum, vendeg1Neve, vendeg2Neve, ar=220, agyszam=2):
        super().__init__(ar, szobaszam)
        self.agyszam=2
        self.foglalt=False
        self.foglDatum=foglDatum
        self.vendeg1Neve=vendeg1Neve
        self.vendeg2Neve=vendeg2Neve
    pass

class Szalloda:
    def __init__(self, nev, szobakEgyAgySzama, szobakKetAgySzama, szobakEgyAgyLista, szobakKetAgyLista):
        self.nev=nev
        self.szobakEgyAgySzama=szobakEgyAgySzama
        self.szobakKetAgySzama=szobakKetAgySzama
        self.szobakEgyAgyLista=szobakEgyAgyLista
        self.szobakKetAgyLista=szobakKetAgyLista
        for i in range(self.szobakEgyAgySzama):
            self.szobakEgyAgyLista.append(EgyagyasSzoba)
            EgyagyasSzoba.szobaszam=i
            EgyagyasSzoba.foglalt=False
        for i in range(self.szobakKetAgySzama):
            self.szobakKetAgyLista.append(KetagyasSzoba)
            KetagyasSzoba.szobaszam=i
            KetagyasSzoba.foglalt=False
    pass

class Foglalas:
    def __init__(self, szobaszam, foglDatum, vendeg, foglID):
        self.szobaszam=szobaszam
        self.foglDatum=foglDatum
        self.vendeg=vendeg
        self.foglID=foglID
    pass


ujSzalloda=Szalloda("Blabla Hotel", 100, 250, [], [])


foglLista=[]

def Foglal():
    print("Köszöntjük a Blabla Hotel foglalási renszerében.")
    agySzam=(int)(input("Egyágyas vagy kétágyas szobát kíván foglalni? "))
    
    foglDatum=None
    switch=1
    while (switch==1):    
            foglDatum=input("Adja meg a foglalás dátumát (formátum: YYY-MM-DD): ")
            try:
                foglDatum=datetime.datetime.strptime(foglDatum, '%Y-%m-%d')
                switch = 0
            except ValueError:
                       print("Nem megfelelő dátum formátum, kérjük írja be újra! ")
                       #Forrás: https://codereview.stackexchange.com/questions/166780/asking-user-input-until-a-valid-datetime-is-given-bloated-try-except-blocks
    
    egyAgyasAr=300
    ketAgyasAr=220

    vn=input("Adja meg a kapcsolattartó vendég nevét: ")
    if(agySzam==1):

        switch=1    
        szobaszam=random.randint (1, ujSzalloda.szobakEgyAgySzama)
        
        while(switch==1):

            for i in ujSzalloda.szobakEgyAgyLista:
                if i.szobaszam==szobaszam and i.foglalt==False:
                    i.foglalt=True
                    switch=0
                    break
                else:
                    szobaszam=random.randint(1, ujSzalloda.szobakEgyAgySzama)
                
        
        print(" ")
        print(f"Az Ön által lefoglalt egyágyas szoba száma: {szobaszam},\
 foglalásának dátuma {foglDatum}, fizetendő: {egyAgyasAr} Ft, a vendég neve: {vn}.")
        Id=uuid.uuid4()
        abc=Foglalas(szobaszam, foglDatum, vn, Id)
        foglLista.append(abc)
        print(f"Foglalásának egyedi azonosítója: \
            {Id}.\
    Kérjük őrizze meg, mert a további ügyintézés során még szüksége lehet rá!")

    elif(agySzam==2):
        
        switch=1
        szobaszam=random.randint(101, ujSzalloda.szobakKetAgySzama)

        while(switch==1):

            for i in ujSzalloda.szobakKetAgyLista:
                if i.szobaszam==szobaszam and i.foglalt==False:
                    i.foglalt=True
                    switch=0
                    break
                else:
                    szobaszam=random.randint(101, ujSzalloda.szobakKetAgySzama)

        print(" ")
        print(f"Az Ön által lefoglalt kétágyas szoba száma: {szobaszam},\
 foglalásának dátuma {foglDatum}, fizetendő: {ketAgyasAr} Ft, a vemdég neve: {vn}.")
        Id=uuid.uuid4()
        abc=Foglalas(szobaszam, foglDatum, vn, Id)
        foglLista.append(abc)
        print(f"Foglalásának egyedi azonosítója: \
            {Id}.\
    Kérjük őrizze meg, mert a további ügyintézés során még szüksége lehet rá!")

    return foglLista
 
    

def Lemondas():
    EgyediAzonosito=input("Kérem, adja meg a lemondani kívánt foglalás egyedi azonosítóját: ")

    for i in foglLista:

        if (str(i.foglID) == EgyediAzonosito):
            for j in ujSzalloda.szobakEgyAgyLista:

                if j.szobaszam == i.szobaszam:
                    j.foglalt==False
                    foglLista.remove(i)
                    print("A foglalás lemondva.")
    
                    return
    
            for k in ujSzalloda.szobakKetAgyLista:

                if k.szobaszam == i.szobaszam:
                    k.foglalt==False
                    foglLista.remove(i)
                    print("A foglalás lemondva.")
                    return               
                    
            
    print("A foglalás nem létezik, ezért nem mondható le.")
    return

            
    
def ListazOsszeset():
    for i in foglLista:
        print(i.foglDatum)
        print(i.foglID)
        print(i.szobaszam)
        print(i.vendeg)
    

def opciók():
        print(" ")
        print(" ")
        print("1-es: Foglalás.")
        print("2-es: Lemondás.")
        print("3-as: Listázás.")
        print("Bármely más szám: Kilépés.")
        
egyFogl=Foglalas(50, 2024-10-14, "Geri", uuid.uuid4())
foglLista.append(egyFogl)  

ketFogl=Foglalas(150, 2024-10-10, "Gabi", uuid.uuid4())
foglLista.append(ketFogl) 

harFogl=Foglalas(78, 2024-11-30, "Tomi", uuid.uuid4())
foglLista.append(harFogl) 

negyFogl=Foglalas(113, 2024-10-19, "Zsuzsi", uuid.uuid4())
foglLista.append(negyFogl) 

otFogl=Foglalas(109, 2024-11-20, "Kovacs", uuid.uuid4())
foglLista.append(otFogl) 


while True:
    try:
        opciók()
        opció = int(input())
        if opció == 1:
            Foglal()
        elif opció == 2:
            Lemondas()
        elif opció == 3:
            ListazOsszeset()
        else:
            print("Viszontlátásra!")
            break

    except:
        break
