def fel1():
    print("1.fel")
    """
    Kérj be a felhasználótól egy szöveget.  Alakítsd nagybetűssé!
    """
    szoveg: str = str(input("Adjon meg egy szöveget!"))
    nSzoveg = szoveg.upper()
    print(nSzoveg)

    """
    Az előző szövegről döntsd el, hogy 10 karakternél hosszabb-e? Ha igen, akkor írd ki a hosszát!
    """
    if len(szoveg) > 10:
        print(f"Szöveg hossza: {len(szoveg)}")


def fel2():
    """
     Kérj be egy legalább 3 betűs szót a felhasználótól. A szavakat addig kérd be, amíg a hossza legalább 3!
    """
    szoveg: str = str(input("Adjon egy szöveget!"))
    while len(szoveg) < 3:
        szoveg: str = str(input("Adjon egy szöveget ,ami hosszabb mint 3!"))


def fel3():
    """
    Kérj be a felhasználótól egy szöveget. Keresd meg benne az első "a" betűt.
    """
    szoveg: str = str(input("Adjon egy szöveget!"))
    print(szoveg.index("a"))
    """
    Hány "a" betű van a bekért szövegben? 
    """
    print(szoveg.count("a"))


def fel4():
    """
    ++ feketeöveseknek: Írd ki, hogy a szöveg egyes betűi hányszor szerepelnek a szövegben?
    """
    szoveg: str = str(input("Adjon egy szöveget!"))
    ossze_betu = {}
    for i in szoveg:
        if i in ossze_betu:
            ossze_betu[i] += 1
        else:
            ossze_betu[i] = 1

