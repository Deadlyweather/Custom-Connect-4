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

leveys, korkeus, määrä = kysy_asetukset()
print("Aloitetaan peli...")
with open("Peli/Lauta", "w") as reset:
    pass
with open("Peli/Lauta","a") as Lauta:
    for X in range(leveys):
        for Y in range(korkeus):
            Lauta.write("#")
        Lauta.write("\n")
print("Lauta on luotu.")
with open("Peli/Lauta") as Lauta:
    pelilauta = []
    for rivi in Lauta:
        print(rivi.strip())
        pelilauta.append(rivi)
while True:
    print("Pelaaja 1 (X)")
    while True:
        try:
            kohde = int(input(f"Pudota (1-{leveys}): "))
            if kohde < 1 or kohde > leveys:
                print(f"Syötä luku välillä 1 ja {leveys}")
                continue
            break
        except ValueError:
            print(f"Syötä kokonaisluku välillä 1 ja {leveys}")
    print("Pelaaja 2 (O)")
    while True:
        try:
            kohde2 = int(input(f"Pudota (1-{leveys}): "))
            if kohde2 < 1 or kohde2 > leveys:
                print(f"Syötä luku välillä 1 ja {leveys}")
                continue
            break
        except ValueError:
            print(f"Syötä kokonaisluku välillä 1 ja {leveys}")

