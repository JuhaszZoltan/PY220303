class Versenyzo:
    def __init__(self, sor: str):
        v = sor.strip().split(';')
        self.nev: str = v[0]
        self.kategoria: bool = v[1] != 'Noi'
        self.egyesulet: str = v[2]
        self.pontok: list = []
        for i in range(3, len(v)):
            self.pontok.append(int(v[i]))
        self.osszpont = 0
        rendezett = self.pontok
        rendezett.sort()
        for i in range(2, len(rendezett)):
            self.osszpont += rendezett[i]
        if rendezett[0] != 0: self.osszpont += 10
        if rendezett[1] != 0: self.osszpont += 10


def nok_aranya(versenyzok : list):
    nok_szama = 0
    for v in versenyzok:
        if not v.kategoria: nok_szama += 1
    return round(nok_szama / len(versenyzok) * 100, 2)


def noi_gyoztes(versenyzok: list) -> Versenyzo:
    maxi = 0
    while versenyzok[maxi].kategoria: maxi += 1
    for i in range(maxi + 1, len(versenyzok)):
        if not versenyzok[i].kategoria:
            if versenyzok[i].osszpont > versenyzok[maxi].osszpont:
                maxi = i
    return versenyzok[maxi]


def ferfiak_fileba(versenyzok: list) -> None:
    file = open(file='osszpontFF.txt', mode='w', encoding='utf-8')
    for v in versenyzok:
        if v.kategoria: file.write(f'{v.nev};{v.osszpont}\n')
    file.close()


def egyesuletek(versenyzok: list) -> None:
    csop: dict = {}
    v: Versenyzo
    for v in versenyzok:
        if v.egyesulet not in csop.keys():
            csop[v.egyesulet] = 1
        else: csop[v.egyesulet] += 1
    for kvp in csop.items():
        if kvp[0] != 'n.a.' and kvp[1] > 2:
            print(f'\t{kvp[0]}: {kvp[1]} fő')

