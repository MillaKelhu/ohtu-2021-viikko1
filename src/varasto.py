class Varasto:
    def __init__(self, tilavuus, alku_saldo=0):
        self.tilavuus = max(0.0, tilavuus)

        if alku_saldo < 0:
            # virheellinen, nollataan
            alku_saldo = 0

        # saldo ei voi olla isompi kuin tilavuus
        alku_saldo = min(alku_saldo, tilavuus)

        self.saldo = alku_saldo

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

        # lisärivejä pylintin testaukseen
        if maara == 1:
            print("maara on 1 :)")
        elif maara == 2:
            print("maara on 2 :)")
        elif maara == 3:
            print("maara on 3 :)")
        elif maara == 4:
            print("maara on 4 :)")
        elif maara == 5:
            print("maara on 5 :)")
        elif maara == 6:
            print("maara on 6 :)")
        elif maara == 7:
            print("maara on 7 :)")
        elif maara == 8:
            print("maara on 8 :)")
        elif maara == 9:
            print("maara on 9 :)")
        else:
            print("Hehheh lol :)")

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
