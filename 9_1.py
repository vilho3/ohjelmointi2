'''
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
 tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
 joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
  Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
  Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
   Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet
'''

class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self. tämänhetkinen_nopeus = 0
        self. kuljettu_matka= 0

def tulostus(auto):
    print("Auton tiedot: ")
    for x, y in auto.__dict__.items():
        print(f"{x},{y}")
    return auto

def main():

    auto=Auto("ABC-123","142 km/h")
    tulostus(auto)


main()