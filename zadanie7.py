import random


def losuj_pogode():
    return random.choice(["pada", "nie pada"])


def sprawdz_pogode():
    pogoda = losuj_pogode()  # Losujemy pogodę
    while True:
        odpowiedz = input("Czy pada deszcz? (tak / nie): ").lower()
        
     
        if odpowiedz == "tak" and pogoda == "pada":
            print("Brawo! Zgadłeś!")
            break
        elif odpowiedz == "nie" and pogoda == "nie pada":
            print("Brawo! Zgadłeś!")
            break
        else:
            print("Nie zgadłeś. Spróbuj ponownie.")


sprawdz_pogode()
