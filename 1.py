import math

def pole_kola(r):
    """Funkcja oblicza i wypisuje pole koła o promieniu r."""
    if r >= 0:
        pole = math.pi * r**2
        print(f"Pole koła o promieniu {r} wynosi {pole:.2f}")
    else:
        print("Promień musi być liczbą dodatnią.")

pole_kola(5)
