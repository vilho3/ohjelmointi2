'''
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
 Jos nopeuden muutos on negatiivinen, auto hidastaa.
  Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
   Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
   Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin
   +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
   Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
    Kuljettua matkaa ei tarvitse vielä päivittää.
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


def main():
    auto=Auto("ABC-123",142)
    auto.kiihdytä(30)
    auto.kiihdytä(50)
    auto.kiihdytä(70)
    print(f"tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus} km/h")
    auto.kiihdytä(-200)
    print(f"tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus} km/h")
main()