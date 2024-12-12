def wspolne_elementy(sekwencja1, sekwencja2):
    """Funkcja zwraca listę wspólnych elementów dwóch sekwencji."""
    return list(set(sekwencja1) & set(sekwencja2))

print(wspolne_elementy([1, 2, 3, 4], [3, 4, 5, 6]))  # Wynik: [3, 4]
