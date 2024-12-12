import math

def pole_trojkata(a, b, c):
    """Funkcja oblicza pole trójkąta na podstawie boków a, b, c."""
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Pole trójkąta wynosi {pole:.2f}")
    else:
        print("Podane długości boków nie tworzą trójkąta.")

pole_trojkata(3, 4, 5)
