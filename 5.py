def srednia(lista):
    """Funkcja oblicza średnią arytmetyczną z listy liczb."""
    if lista:
        wynik = sum(lista) / len(lista)
        print(f"Średnia wynosi {wynik:.2f}")
    else:
        print("Lista jest pusta.")

srednia([1, 2, 3, 4, 5])
