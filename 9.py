def fib(n):
    """Funkcja rekurencyjna oblicza n-ty wyraz ciągu Fibonacciego."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(6))  # Wynik: 8
