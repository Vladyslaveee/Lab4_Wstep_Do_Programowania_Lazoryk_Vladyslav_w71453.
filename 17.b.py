def znajdz_max(*args):
    """Funkcja zwraca maksymalną wartość spośród przekazanych parametrów."""
    if args:
        return max(args)
    else:
        return None

print(znajdz_max(1, 2, 3, 10, 5))  # Wynik: 10
