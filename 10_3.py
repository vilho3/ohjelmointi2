'''
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
 joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
'''


class Hissi:
    def __init__(self,alin_kerros,ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros+=1
            print(f"olet kerroksessa: {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"olet kerroksessa: {self.nykyinen_kerros}")


    def siirry_kerrokseen(self, kerros_siirtymä):
        if kerros_siirtymä > self.ylin_kerros or kerros_siirtymä < self.alin_kerros:
            print("Et pääse sinne")

        while self.nykyinen_kerros > kerros_siirtymä:
            self.kerros_alas()
        while self.nykyinen_kerros < kerros_siirtymä:
            self.kerros_ylös()
        return

class Talo:
    def __init__(self,alin_kerros,ylin_kerros, hissien_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lukumäärä = hissien_lukumäärä
        self.hissit=[]
        self.hissi=0

        for i in range(self.hissien_lukumäärä):
            self.hissi+=1
            self.hissit.append(Hissi(self.alin_kerros,self.ylin_kerros))

    def aja_hissiä(self,hissin_numero,kohdekerros):
        if 1<=hissin_numero <= len(self.hissit):
            hissi=self.hissit[hissin_numero-1]
            print(f"Ajetaan hissillä: {hissin_numero} kerrokseen: {kohdekerros}")
            hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for i in range(len(self.hissit)):
            print("PALOHÄLYTYS: hissit siirtyvät pohjakerrokseen: ")
            hissi=self.hissit[i]
            hissi.siirry_kerrokseen(self.alin_kerros)



def main():
   # h=Hissi(1,6 )
   # print(f"olet nyt kerroksessa : {h.nykyinen_kerros}")
    t=Talo(1,6,2)
    t.aja_hissiä(1,4)
    t.aja_hissiä(2,2)
    t.palohälytys()

main()


