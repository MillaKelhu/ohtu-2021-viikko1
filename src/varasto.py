class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = max(0.0, tilavuus)

        # saldo ei voi olla pienempi kuin 0
        alku_saldo = max(alku_saldo, 0)

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
