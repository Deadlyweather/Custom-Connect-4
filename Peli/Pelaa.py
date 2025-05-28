def kysy_asetukset():
    print("Settings: ")
    while True:
        try:
            leveys = int(input("Anna leveys: "))
            korkeus = int(input("Anna korkeus: "))
            määrä = int(input("Anna määrä: "))
        except ValueError:
            print("Syötä kokonaisluku!")
            continue
        if input("Oletko tyytyväinen valintoihisi? (k/e): ").lower() == 'k':
            break
    return leveys, korkeus, määrä

leveys, korkeus, maara = kysy_asetukset()
print("Aloitetaan peli...")
with open("Peli/Settings.py", "w") as reset:
    pass
with open("Peli/Lauta","a") as Lauta:
    for X in range(leveys):
        for Y in range(korkeus):
            Lauta.write("#")
        Lauta.write("\n")
print("Lauta on luotu.")
with open("Peli/Lauta") as Lauta:
    for rivi in Lauta:
        print(rivi.strip())
while True:
    print("pelaaja 1")
    kohde = int(input(f"Pudota (1-{leveys})"))