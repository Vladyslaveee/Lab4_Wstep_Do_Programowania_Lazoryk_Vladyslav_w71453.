def przedstaw_sie(imie, wiek=18):
    """
    Funkcja wypisuje imię i wiek podane jako parametry.
    Wiek ma wartość domyślną 18.
    """
    print(f"Cześć, mam na imię {imie}, a mój wiek to {wiek}.")

print(przedstaw_sie.__doc__)
przedstaw_sie("Yevheniia")
przedstaw_sie("Vladyslav", 17)
