'''
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
'jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa
eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
kun kilpailu on päättynyt.
'''

import random

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

class Kilpailu:
    def __init__(self,kilpailun_nimi, pituus_kilometreinä, osallistuvat_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_kilometreinä = pituus_kilometreinä
        self.osallistuvat_autot=osallistuvat_autot
        self.tunnit=0

    def tunti_kuluu(self):
        for auto in self.osallistuvat_autot:
            auto.kulje(1)
            auto.kiihdytä(+random.randint(-10, 15))
        self.tunnit+=1

    def tulosta_tilanne(self):
        print(f"Tilanne {self.tunnit} tunnin jälkeen")
        for auto in self.osallistuvat_autot:
            print(f"{auto.rekisteritunnus} kuljettu matka: {auto.kuljettu_matka} km, tämänhetkinen nopeus:"
                  f" {auto.tämänhetkinen_nopeus} km/h, huippunopeus: {auto.huippunopeus} km/h\n")

    def kilpailu_ohi(self):
        for auto in self.osallistuvat_autot:
           if auto.kuljettu_matka >= self.pituus_kilometreinä:
              return True
        else:
            return False



def main():
    lista=[]
    for i in range(1,11):
        rekisteritunnus=f"ABC-{i}"
        huippunopeus=random.randint(100,200)
        auto=Auto(rekisteritunnus, huippunopeus)
        lista.append(auto)

    k=Kilpailu("Suuri romuralli",8000,lista)

    while not k.kilpailu_ohi():
        k.tunti_kuluu()
        if k.tunnit % 10==0:
            k.tulosta_tilanne()
    k.tulosta_tilanne()
    print("Kilpailu päättyi")
main()