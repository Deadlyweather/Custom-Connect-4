import Settings
print("Settings: ")
while True:
    Valinnat = Settings.Settings(input("Anna leveys: "), input("Anna korkeus: "), input("Anna määrä: "))
    print(Valinnat)
    if input("Oletko tyytyväinen valintoihisi?: ").lower() == 'kyllä':
        break
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