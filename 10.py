def wieza_hanoi(n, start, cel, pomocnik):
    """Funkcja rekurencyjna rozwiązująca problem wieży Hanoi."""
    if n == 1:
        print(f"Przenieś krążek z {start} na {cel}")
    else:
        wieza_hanoi(n - 1, start, pomocnik, cel)
        print(f"Przenieś krążek z {start} na {cel}")
        wieza_hanoi(n - 1, pomocnik, cel, start)

wieza_hanoi(3, 'A', 'C', 'B')
