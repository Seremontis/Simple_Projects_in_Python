# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:33:28 2019

@author: komp2
"""

class Plansza():
    
    def __init__(self,dlugosc,szerokosc):
        self.__planszaUser=[["-" for x in range(szerokosc)] for x in range(dlugosc)]
        self.__planszaUkryta=[["-" for x in range(szerokosc)] for x in range(dlugosc)]
        self.__numerStatku=0
        self.__zatopione=0
        
    def rysuj(self):
        print("====================")
        print("Plansza:")
 
        for wiersz in self.__planszaUser:
            for element in wiersz:
                print(element, end=" ")
            print()
        print("====================")
        
    def dodajStatek(self,x,y,w):
        if(len(self.__planszaUser[0])<w):
            return print("Statek jest za duży na mapę")
        if(y+w>len(self.__planszaUser[0])):
            return 'Statek wykracza poza mapę'
        
        for i in range(w):
            if(self.__planszaUkryta[x][i]!='-'):
                return print("Pole jest zajęte")  
             
        for i in range(w):
            if(w==1):
                self.__planszaUkryta[x][i]='J'+str(self.__numerStatku)
            elif(w==2):
                 self.__planszaUkryta[x][i]='D'+str(self.__numerStatku)
            elif(w==4):
                 self.__planszaUkryta[x][i]='C'+str(self.__numerStatku)
            
        self.__numerStatku+=1

    def pokazUkryta(self):
        print("====================")
        print("Ukryta:")
 
        for wiersz in self.__planszaUkryta:
            for element in wiersz:
                print(element, end=" ")
            print()
        print("====================")
        
    def strzel(self,x,y):
        if self.__planszaUkryta[x][y]=='-':
            self.__planszaUser[x][y]='P'
        elif self.__planszaUser[x][y]=='P' or self.__planszaUser[x][y]=='T':
            return print('Pole zostało już wczesniej wybrane')
        else:
            self.__planszaUser[x][y]='T'
            self.sprawdzZatopienie(x,y)
        print('{} z {}'.format(self.__zatopione,self.__numerStatku))
        if self.__numerStatku==self.__zatopione:
            return print('Zatopiono wszystkie statki. Koniec gry')
            
    def sprawdzZatopienie(self,x,y):
        ile=0
        w=self.__planszaUkryta[x][y]
        statek=''
        rozmiar=0
        if 'J' in w:
            self.__zatopione+=1
            return print('Zatopiłes mały statek')
        elif 'D' in w:
            rozmiar=2
            statek='sredni'
        elif 'C' in w:
            rozmiar=4
            statek='duzy'
        index=0
        for el in self.__planszaUkryta[x]:
            if el==w and self.__planszaUser[x][index]=='T':
                ile+=1
            index+=1
        if ile==rozmiar:
            self.__zatopione+=1
            return print('Zatopiłes {} statek '.format(statek))
    
        
        
p=Plansza(3,4)
#p.rysuj()
p.dodajStatek(0,0,2)
p.dodajStatek(1,0,4)
p.strzel(1,0)
p.strzel(0,1)
p.strzel(0,0)
p.strzel(1,1)
p.strzel(1,2)
p.strzel(1,3)
p.rysuj()
p.pokazUkryta()