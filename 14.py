def nwd(a, b):
    """Funkcja oblicza największy wspólny dzielnik dwóch liczb."""
    while b:
        a, b = b, a % b
    return a

print(nwd(48, 18))  # Wynik: 6
