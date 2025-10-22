'''
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton
(ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran
ja tulosta autojen matkamittarilukemat.
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

class Sähköauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus,huippunopeus)


class Polttoauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,bensatankinkoko):
        self.bensatankinkoko = bensatankinkoko
        super().__init__(rekisteritunnus,huippunopeus)



def main():
    sauto=Sähköauto("ABC-15",180,52.5)
    pauto=Polttoauto("ACD-123",160,32.3)
    sauto.tämänhetkinen_nopeus=100
    pauto.tämänhetkinen_nopeus=120
    sauto.kulje(3)
    pauto.kulje(3)
    print(f"Sähköauton kulkema matka: {sauto.kuljettu_matka} km")
    print(f"Polttomoottoriauton kulkema matka: {pauto.kuljettu_matka} km")
main()