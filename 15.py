def czy_palindrom(slowo):
    """Funkcja sprawdza, czy dane słowo jest palindromem."""
    slowo = slowo.lower().replace(" ", "")  # Ignoruje wielkość liter i spacje
    return slowo == slowo[::-1]

print(czy_palindrom("kajak"))  # Wynik: True
print(czy_palindrom("Python"))  # Wynik: False
