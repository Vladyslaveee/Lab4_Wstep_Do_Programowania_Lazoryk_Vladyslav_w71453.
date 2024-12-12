def okresl_plec(imie):
    """Funkcja określa płeć na podstawie imienia."""
    if imie[-1] == 'a':  # W języku polskim większość imion żeńskich kończy się na 'a'
        return "kobieta"
    else:
        return "mężczyzna"

imiona = ["Anna", "Piotr", "Maria", "Jan", "Katarzyna"]
slownik_plec = {imie: okresl_plec(imie) for imie in imiona}
print(slownik_plec)
