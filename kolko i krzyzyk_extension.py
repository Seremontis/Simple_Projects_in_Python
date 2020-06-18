# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:19:31 2019

@author: komp2
"""

class Plansza:
    def __init__(self, wielkosc):
        self.__plansza = [["-" for x in range(wielkosc)] for x in range(wielkosc)]
        self.__symbol = False # True - X, False - O
        self.__skreslenia=[0,0]
 
    def wyswietl(self):
        print("==========")
        print("Plansza:")
 
        for wiersz in self.__plansza:
            for krotka in wiersz:
                print(krotka, end=" ")
            print()
        print("==========")
 
    def __dajSymbol(self):
        if self.__symbol:
            return "X"
        return "O"
 
    def __sprawdzPole(self, wiersz, kolumna):
        if len(self.__plansza)<wiersz:
            return False
        if len(self.__plansza[wiersz])<kolumna:
            return False
        if(self.__plansza[wiersz][kolumna]!='-'):
            return False
        return True
    
    def zagraj(self, wiersz, kolumna):
        if not self.__sprawdzPole(wiersz, kolumna):
            print("Błędne pole")
            return -1

        self.__symbol = not self.__symbol
        self.__plansza[wiersz][kolumna]=self.__dajSymbol()
 
        self.sprawdzCzySkreslc(wiersz,kolumna)
        if self.czyNieMaPustychPol():
            if(self.__skreslenia[1]<self.__skreslenia[0]):
                return 1 #Wygrana X
            elif(self.__skreslenia[1]>self.__skreslenia[0]):
                return 2 #Wygrana 0
            else:
                return 3 #Remis
        return 0 
    
    def czyNieMaPustychPol(self):
        for i in range(len(self.__plansza)):
            for z in range(len(self.__plansza[i])):
                if self.__plansza[i][z]=='-':
                    return False
        return True

    # Sprawdzenie czy znajduję się 5 elementów koło siebie
    def sprawdzCzySkreslc(self,wiersz,kolumna):
        return self.czySkreslicPoziomo(wiersz,kolumna) or self.czySkreslicPionowo(wiersz,kolumna) or self.czySkreslicUkos(wiersz,kolumna)
            
    
    
    def czySkreslicPoziomo(self,wiersz,kolumna):
        symbol=self.__dajSymbol()
        countSymbol1=0
        countSymbol2=0
        if kolumna>0:
            index=kolumna-1
            while index>=0 and self.__plansza[wiersz][index]==symbol:
                    countSymbol1+=1
                    index-=1      
        if kolumna<len(self.__plansza)-1:
            index=kolumna+1
            while index<len(self.__plansza) and self.__plansza[wiersz][index]==symbol:
                    countSymbol2+=1  
                    index+=1
        if countSymbol1+countSymbol2+1>=5:
            if(symbol=='X'):
                self.__skreslenia[0]+=1
            else:
                self.__skreslenia[1]+=1
            if countSymbol1>=2 and countSymbol2>=2:
                for i in range(kolumna-2,kolumna+3,1):
                    self.__plansza[wiersz][i]='N'
            else:
                start=kolumna
                if countSymbol2<2 and countSymbol1!=0:
                    start-=countSymbol1
                elif countSymbol1<2:
                    start-=(4-countSymbol2)
                for i in range(start,start+5,1):
                    self.__plansza[wiersz][i]='N'
            return True
        return False
    
    def czySkreslicPionowo(self,wiersz,kolumna):
        symbol=self.__dajSymbol()
        countSymbol1=0
        countSymbol2=0
        if wiersz>0:
            index=wiersz-1
            while index>=0 and self.__plansza[index][kolumna]==symbol:
                    countSymbol1+=1
                    index-=1      
        if wiersz<len(self.__plansza)-1:
            index=wiersz+1
            while index<len(self.__plansza) and self.__plansza[index][kolumna]==symbol:
                    countSymbol2+=1  
                    index+=1
        if countSymbol1+countSymbol2+1>=5:
            if(symbol=='X'):
                self.__skreslenia[0]+=1
            else:
                self.__skreslenia[1]+=1
            if countSymbol1>=2 and countSymbol2>=2:
                for i in range(wiersz-2,wiersz+3,1):
                    self.__plansza[i][kolumna]='N'
            else:
                start=wiersz
                if countSymbol2<2 and countSymbol1!=0:
                    start-=countSymbol1
                elif countSymbol1<2:
                    start-=(4-countSymbol2)
                for i in range(start,start+5,1):
                    print(i)
                    self.__plansza[i][kolumna]='N'
            return True
        return False
    
    def czySkreslicUkos(self,wiersz,kolumna):
        symbol=self.__dajSymbol()
        countSymbol1=0
        countSymbol2=0
        odwrukos=False;
        if kolumna>=0 and wiersz>=0:
            indexK=kolumna-1
            indexW=wiersz-1
            while indexK>=0 and indexW>=0 and self.__plansza[indexW][indexK]==symbol:
                    countSymbol1+=1
                    indexK-=1
                    indexW-=1
        if kolumna<len(self.__plansza)-1 and wiersz<len(self.__plansza)-1:
            indexK=kolumna+1
            indexW=wiersz+1
            while indexK>=0 and indexW>=0 and indexK<len(self.__plansza) and indexW<len(self.__plansza) and self.__plansza[indexW][indexK]==symbol:
                    countSymbol2+=1
                    indexK+=1
                    indexW+=1
        if(countSymbol1+countSymbol2+1<5):   
            if kolumna<=len(self.__plansza)-1 and wiersz>=0:
                indexK=kolumna-1
                indexW=wiersz+1
                while indexK>=0 and indexW>=0 and indexK<=len(self.__plansza)-1 and indexW<=len(self.__plansza)-1 and self.__plansza[indexW][indexK]==symbol:
                        countSymbol2+=1
                        indexK-=1
                        indexW+=1
                odwrukos=True            
        if countSymbol1+countSymbol2+1>=5:
            if(symbol=='X'):
                self.__skreslenia[0]+=1
            else:
                self.__skreslenia[1]+=1
            if countSymbol1>=2 and countSymbol2>=2:
                indexK=kolumna-2
                for i in range(wiersz-2,wiersz+3,1):
                    self.__plansza[i][indexK]='N'
                    indexK+=1
            else:
                start=wiersz
                indexK=kolumna
                if countSymbol2<2 and countSymbol1!=0:
                    start-=countSymbol1
                    indexK-=countSymbol1
                elif countSymbol1<2:
                    start-=(4-countSymbol2)
                    indexK-=(4-countSymbol2)
                for i in range(start,start+5,1):
                    self.__plansza[i][indexK]='N'
                    if odwrukos:
                        indexK-=1
                    else:
                        indexK+=1                                       
            return True
        return False          
       #koniec sprawdzania koło siebie         
                
p = Plansza(6)
p.wyswietl()
 
p.zagraj(0, 0)
p.wyswietl()

p.zagraj(5, 0)
p.wyswietl()

p.zagraj(1, 1)
p.wyswietl()
p.zagraj(4, 0)
p.wyswietl()

