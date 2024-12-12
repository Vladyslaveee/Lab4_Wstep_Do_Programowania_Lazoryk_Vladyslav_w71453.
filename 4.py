def oblicz_bmi(waga, wzrost):
    """Funkcja oblicza BMI i informuje o jego zakresie."""
    if wzrost > 0:
        bmi = waga / (wzrost ** 2)
        print(f"Twoje BMI wynosi {bmi:.2f}")
        if bmi < 18.5:
            print("Niedowaga")
        elif 18.5 <= bmi < 25:
            print("Prawidłowa waga")
        elif 25 <= bmi < 30:
            print("Nadwaga")
        else:
            print("Otyłość")
    else:
        print("Wzrost musi być większy od zera.")

oblicz_bmi(70, 1.75)
