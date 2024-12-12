def potega_rekurencyjna(a, n):
    """Funkcja rekurencyjna oblicza n-tą potęgę liczby a."""
    if n == 0:
        return 1
    else:
        return a * potega_rekurencyjna(a, n - 1)

print(potega_rekurencyjna(2, 3))  # Wynik: 8
