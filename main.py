import module as m

versenyzok = []
for s in open('fob2016.txt', encoding='utf-8'):
    versenyzok.append(m.Versenyzo(s))

# 3. feladat:
print(f'3. feladat: Versenyzők száma: {len(versenyzok)}')

# 4. feladat:
print(f'4. feladat: Női versenyzők aránya: {m.nok_aranya(versenyzok)}%')

# 6. feladat:
gyoztes_no = m.noi_gyoztes(versenyzok)
print('6. feladat: A bajnok női versenyző:')
print(f'\tNév: {gyoztes_no.nev}')
print(f'\tEgyesület: {gyoztes_no.egyesulet}')
print(f'\tÖsszpont: {gyoztes_no.osszpont}')

# 7. feladat
m.ferfiak_fileba(versenyzok)

#8. feladat:
print('8. feladat: Egyesület statisztika')
m.egyesuletek(versenyzok)