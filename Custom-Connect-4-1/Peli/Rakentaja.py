import Settings
with open("Peli/Settings.py", "w") as reset:
    pass
with open("Peli/Lauta","a") as Lauta:
    for X in range(Settings.leveys):
        for Y in range(Settings.korkeus):
            Lauta.write("#")
        Lauta.write("\n")

