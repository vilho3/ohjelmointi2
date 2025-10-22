'''
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
'''


class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdytä(self, muutos):
        self.tämänhetkinen_nopeus+=muutos
        if self.tämänhetkinen_nopeus>self.huippunopeus:
            self.tämänhetkinen_nopeus=self.huippunopeus
        if self.tämänhetkinen_nopeus<0:
            self.tämänhetkinen_nopeus=0
    def kulje(self, tunti):
        self.kuljettu_matka+=tunti* self.tämänhetkinen_nopeus



def main():
    auto=Auto("ABC-123",142)
    auto.kiihdytä(30)
    auto.kiihdytä(50)
    auto.kiihdytä(70)
    auto.kulje(2)
    print(f"kuljettu: {auto.kuljettu_matka} km")
    print(f"tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus} km/h")
   # auto.kiihdytä(-200)
   # print(f"tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus} km/h")
main()