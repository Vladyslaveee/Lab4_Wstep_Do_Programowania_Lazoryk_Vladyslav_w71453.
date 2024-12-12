def pole_trapezu(a, b, h):
    """Funkcja oblicza pole trapezu o podstawach a i b oraz wysokości h."""
    if a > 0 and b > 0 and h > 0:
        pole = ((a + b) * h) / 2
        print(f"Pole trapezu wynosi {pole:.2f}")
    else:
        print("Wszystkie wymiary muszą być dodatnie.")

pole_trapezu(5, 7, 3)

