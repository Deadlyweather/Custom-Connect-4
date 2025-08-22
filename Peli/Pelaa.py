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
        if määrä > leveys or määrä > korkeus:
            print("Määrä ei voi olla suurempi kuin leveys tai korkeus!")
            continue
        if input("Oletko tyytyväinen valintoihisi? (k/e): ").lower() == 'k':
            break
    return leveys, korkeus, määrä

leveys, korkeus, määrä = kysy_asetukset()
print("Aloitetaan peli...")

with open("Lauta", "w") as Lauta:
    for _ in range(korkeus):
        Lauta.write("." * leveys + "\n")

print("Lauta on luotu.")

with open("Lauta") as Lauta:
    pelilauta = [list(rivi.strip()) for rivi in Lauta]

def tulosta_pelilauta():
    print(" " + " ".join(str(i+1) for i in range(leveys))) 
    for rivi in pelilauta:
        print(" " + " ".join(rivi))

def pudota_pelimerkki(sarake, merkki):
    for rivi in reversed(pelilauta):
        if rivi[sarake] == ".":
            rivi[sarake] = merkki
            return True
    print("Sarake on täynnä!")
    return False

def tarkista_voitto(merkki):
    for y in range(korkeus):
        for x in range(leveys):
            if pelilauta[y][x] != merkki:
                continue

            if x + määrä <= leveys and all(pelilauta[y][x + i] == merkki for i in range(määrä)):
                return True

            if y + määrä <= korkeus and all(pelilauta[y + i][x] == merkki for i in range(määrä)):
                return True

            if x + määrä <= leveys and y + määrä <= korkeus and all(pelilauta[y + i][x + i] == merkki for i in range(määrä)):
                return True

            if x - määrä >= -1 and y + määrä <= korkeus and all(pelilauta[y + i][x - i] == merkki for i in range(määrä)):
                return True

    return False

def täysi():
    return all(merkki != "." for rivi in pelilauta for merkki in rivi)

tulosta_pelilauta()
vuoro = 0
while True:
    pelaaja = "X" if vuoro % 2 == 0 else "O"
    print(f"Pelaaja {1 if pelaaja == 'X' else 2} ({pelaaja})")
    while True:
        try:
            kohde = int(input(f"Pudota (1-{leveys}): ")) - 1
            if kohde < 0 or kohde >= leveys:
                print(f"Syötä luku välillä 1 ja {leveys}")
                continue
            if pudota_pelimerkki(kohde, pelaaja):
                break
        except ValueError:
            print(f"Syötä kokonaisluku välillä 1 ja {leveys}")

    tulosta_pelilauta()

    if tarkista_voitto(pelaaja):
        print(f"Pelaaja {1 if pelaaja == 'X' else 2} VOITTI!")
        break

    if täysi():
        print("Tasapeli!")
        break

    vuoro += 1

