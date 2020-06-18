# -*- coding: utf-8 -*-
import random

class Plansza:
    def __init__(self):
        self._plansza = [["_" for x in range(9)] for x in range(9)]
        self._licznik=0
        self._sciezka=""
            
    """Sprawdzanie dostepnosci wartosc"""    
    def sprawdzWPionie(self,y,wartosc):
        for i in range(len(self._plansza)):          
            if(self._plansza[i][y]==wartosc):
                return False
        return True
              
    def sprawdzWPoziomie(self,x,wartosc):
        for i in range(len(self._plansza)):     
            print("[{}{}] {}".format(x,i,wartosc))
            if(self._plansza[x][i]==wartosc):
                return False
        return True
        
    def sprawdzNaKwadracie(self,x,y,wartosc):
        moduloX=x%3
        moduloY=y%3
        startX=x-moduloX
        startY=y-moduloY
        for i in range(startX,startX+3):
            for z in range(startY,startY+3):
                if(self._plansza[i][z]==wartosc):
                    return False
        return True
    
    def sprawdzLiczbe(self,wartosc):
        if wartosc>0 and wartosc<10:
            return True
        else:
            print("Nieprawidłowa liczba")
            return False
        
        
    """Funkcje dostepne dla uzytkownika"""
    def wyswietl(self):
        x=0
        y=0
        print("==========")
        print("Obecna sytuacja na planszy:")
        for wiersz in self._plansza:
            if(x==3):
                print("--------------------")
                x=0
            x+=1
            y=0
            for krotka in wiersz:
                if(y==3):
                    print("|",end="")
                    y=0
                y+=1
                print(krotka, end=" ")
            print()
        print("==========")    
    
    
    def nastepnyRuch(self,x,y,wartosc):
        if self.sprawdzLiczbe(wartosc):
            if(self._plansza[x][y]=="_"):
                if self.sprawdzWPionie(y,wartosc) and self.sprawdzWPoziomie(x,wartosc) and self.sprawdzNaKwadracie(x,y,wartosc):
                    self._plansza[x][y]=str(wartosc)
                    self._licznik+=1           
                else:
                    print("Wartosc nieprawidlowa o wspolrzednych [{},{}] i wartosci {}".format(x,y,wartosc))
            else:
                print("Pole jest zajete")
        if self._licznik==81:
            print("Gra zakonczona")
        
    def wypelnijLosowoPola(self,liczbaMaxPolLos):
        if(liczbaMaxPolLos<16):
            for i in range(liczbaMaxPolLos):
                x=random.randint(0, 8)
                y=random.randint(0, 8)
                wartosc=random.randint(1, 9)
                if(self._plansza[x][y]=="_"):
                    if self.sprawdzWPionie(y,wartosc) and self.sprawdzWPoziomie(x,wartosc) and self.sprawdzNaKwadracie(x,y,wartosc):
                        self._plansza[x][y]=wartosc
                        self._licznik+=1 
        else:
            print ("Losowa liczba pól jest za duża.")
                 
    def zapiszDoPliku(self,sciezka=""):
        if(sciezka!=""):
            self._sciezka=sciezka
        elif(sciezka!="" and self._sciezka==""):
            print("Brak sciezki do zapisania pliku")
        newfile=open(self._sciezka,"w")
        for wiersz in self._plansza:
            for val in wiersz:
                newfile.write(str(val))
            newfile.write("\n")
        newfile.close()

    def wczytajZapis(self,sciezka=""):
        if(sciezka!=""):
            self._sciezka=sciezka
        elif(sciezka!="" and self._sciezka==""):
            print("Brak sciezki do wczytania pliku")            
        with open(self._sciezka,"r") as f:
            x=0
            for line in f:     
                for y in range(len(self._plansza)):
                    if(line[y]=="_"):
                        self._plansza[x][y]=line[y]
                    else:
                        self._plansza[x][y]=int(line[y])
                x+=1
        
        
#plansza=Plansza()
#plansza.wyswietl()
#plansza.nastepnyRuch(0,0,1)
#plansza.nastepnyRuch(0,1,9)
#plansza.nastepnyRuch(1,1,7)
#plansza.nastepnyRuch(1,2,2)
#plansza.nastepnyRuch(0,2,3)
#plansza.nastepnyRuch(8,2,1)
#plansza.nastepnyRuch(7,1,1)
#plansza.nastepnyRuch(7,7,1)
#plansza.wyswietl()


planszaLos=Plansza()
#planszaLos.wypelnijLosowoPola(10)
#planszaLos.wyswietl()
#planszaLos.zapiszDoPliku(r"C:\temp\sudokusave.txt")
planszaLos.wczytajZapis(r"C:\temp\sudokusave.txt")
planszaLos.nastepnyRuch(0,1,7)
planszaLos.wyswietl()