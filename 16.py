def czy_anagram(slowo1, slowo2):
    """Funkcja sprawdza, czy dwa słowa są anagramami."""
    return sorted(slowo1.lower()) == sorted(slowo2.lower())

print(czy_anagram("tok", "kot"))  # Wynik: True
print(czy_anagram("python", "java"))  # Wynik: False
