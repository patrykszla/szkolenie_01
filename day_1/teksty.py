tekst = 'Witaj świecie'
print(tekst)
print(type(tekst))

print(tekst.upper())
print(tekst.capitalize())
print(tekst.swapcase())

# indeksy w tekście od 0
print(tekst[6])
print(tekst.index('i'))  # indeks dla i
print(tekst.count('i'))  # ile razy występuje
print(tekst.count("j", 0, 4))
print(tekst.removeprefix("Witaj"))
print(tekst.removesuffix("świecie"))
print(tekst.removesuffix("świecie").strip())

name = "    PATRYK   "
print(name.rstrip())
print(name.lstrip())

tekst_zamiana = "Witaj Dobry Świecie"
print(tekst_zamiana.replace("Dobry", ""))

encode_s = tekst.encode('utf-8')
print(encode_s)
print(type(encode_s))
print(encode_s.decode('utf-8'))

imie = "Patryk"
# f string
tekst_format = f"Mam na imię {imie} "
print(tekst_format)

tekst_format = f"\t Mam na imię {imie}\n i siema siema.\b"

print(tekst_format)

starszy = "Witaj %s!"
print(starszy % imie)

print("Witaj {}!".format(imie))  # nie używać!!!!!

print("Witaj", imie, "!")

print("""Tekst
        wielolinijkowy""")

"""Komentarz
 wielolinijkowy"""
