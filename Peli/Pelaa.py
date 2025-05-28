def kysy_asetukset():
    print("Settings: ")
    while True:
        try:
            leveys = int(input("Anna leveys: "))
            korkeus = int(input("Anna korkeus: "))
            maara = int(input("Montako peräkkäin voittaa?: "))
        except ValueError:
            print("Syötä kokonaisluku!")
            continue
        if input("Oletko tyytyväinen valintoihisi? (k/e): ").lower() == 'k':
            break
    return leveys, korkeus, maara
print("Aloitetaan peli...")
with open("Peli/Settings.py", "w") as reset:
    pass
with open("Peli/Lauta","a") as Lauta:
    for X in range(Settings.leveys):
        for Y in range(Settings.korkeus):
            Lauta.write("#")
        Lauta.write("\n")
print("Lauta on luotu.")
with open("Peli/Lauta") as Lauta:
    for rivi in Lauta:
        print(rivi.strip())
