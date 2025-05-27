class Settings:
    def __init__(self):
        self.settings = {}
    def lauta(self, leveys, korkeus):
        self.leveys = leveys
        self.korkeus = korkeus
    def voiton_ehto(self, määrä):
        self.määrä = määrä
    #Tämä on olemassa koska pelin nimi on Custom
