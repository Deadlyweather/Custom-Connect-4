class Settings:
    def __init__(self, leveys=8, korkeus=8, määrä=4):
        self.leveys = leveys
        self.korkeus = korkeus
        self.määrä = määrä
    def __str__(self):
        return f"Leveys: {self.leveys}, Korkeus: {self.korkeus}, Määrä: {self.määrä}"