class ElementZamowienia:
    nazwa=''
    cena=0
    liczbaSztuk=0
    def __init__(self,nazwa='',cena=0.00,liczbaSztuk=0):
        self.nazwa=nazwa
        self.cena=cena
        self.liczbaSztuk=liczbaSztuk
        
    def __str__(self):
        return '{} {} zł, {} szt., łącznie {} zł'.format(self.nazwa,self.cena,self.liczbaSztuk,self.cena*self.liczbaSztuk)
    
    def obliczKoszt(self):
        wartosc=self.cena*self.liczbaSztuk
        return [wartosc-(wartosc*self.obliczRabat()),wartosc*self.obliczRabat()]
    
    def obliczRabat(self):
        if self.liczbaSztuk>=5:
            return 0.1
        else:
            return 0
    
class Zamowienie:
    elementy=[]
    rozmiar=0
    maksRozmiar=0
    
    def __init__(self,maksRozmiar):
        self.maksRozmiar=maksRozmiar
        
    def dodaj(self,elZam):
        if len(self.elementy)<self.maksRozmiar:
            self.elementy.append(elZam)
            return True
        else:
            return False
        
    def obliczKoszt(self):
        lacznie=0
        rabat=0
        for el in self.elementy:
            tmp=el.obliczKoszt()
            lacznie+=tmp[0]
            rabat+=tmp[1]
        return [lacznie,rabat]
    def pisz(self):
        print('Zamówienie:')
        for i in range(len(self.elementy)):
            print('{0}. {1}, {2} zł, {3} szt., łącznie {4} zł'.format(i+1,self.elementy[i].nazwa,self.elementy[i].cena,self.elementy[i].liczbaSztuk,self.elementy[i].obliczKoszt()[0]))
        wynik=self.obliczKoszt()
        print('Koszt całkowity: {} zł \nNaliczony rabat {} zł'.format(wynik[0],wynik[1]))
        
z = Zamowienie(10)
z.dodaj(ElementZamowienia("Chleb", 4.0, 2))
z.dodaj(ElementZamowienia("Mleko", 2.5, 1))
z.dodaj(ElementZamowienia("Cukier", 4.0, 5))
z.dodaj(ElementZamowienia("Puszka", 9.0, 1))
z.pisz()
