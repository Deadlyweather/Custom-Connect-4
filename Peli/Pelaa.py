import Settings
print("Settings:")
while True:
    Valinnat = Settings.Settings(input("Anna leveys: "), input("Anna korkeus: "), input("Anna määrä: "))
    print(Valinnat)
    if input("Oletko tyytyväinen valintoihisi?: ").lower() == 'kyllä':
        break
while True:
    print("pelaaja 1:")