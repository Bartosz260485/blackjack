import random

#SŁOWNIKI I DANE PODSTAWOWE
WARTOSCI_KART = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Walet': 10, 'Dama': 10, 'Król': 10, 'As': 11
}

KOLORY = ['Pik', 'Kier', 'Trefl', 'Karo']
FIGURY = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Walet', 'Dama', 'Król', 'As']


#FUNKCJE GRY

def stworz_i_potasuj_talie():
    talia = []
    for kolor in KOLORY:
        for figura in FIGURY:
            karta = f"{figura} {kolor}"
            talia.append(karta)

    random.shuffle(talia)
    return talia


def oblicz_punkty(reka):
    punkty = 0
    liczba_asow = 0

    for karta in reka:
        figura = karta.split()[0]
        punkty += WARTOSCI_KART[figura]

        if figura == 'As':
            liczba_asow += 1

    while punkty > 21 and liczba_asow > 0:
        punkty -= 10
        liczba_asow -= 1

    return punkty


#GŁÓWNA PĘTLA GRY

def zagraj_w_blackjacka():
    print("=== WITAJ W KASYNIE ===")

    talia = stworz_i_potasuj_talie()
    reka_gracza = []
    reka_krupiera = []

    for _ in range(2):
        reka_gracza.append(talia.pop())
        reka_krupiera.append(talia.pop())

    koniec_gry = False

    # TURA GRACZA
    while not koniec_gry:
        punkty_gracza = oblicz_punkty(reka_gracza)

        print(f"\nTwoje karty: {reka_gracza} (Punkty: {punkty_gracza})")
        print(f"Karta krupiera: [{reka_krupiera[0]}] i [Ukryta karta]")

        if punkty_gracza == 21:
            print("Blackjack! Wygrywasz!")
            return
        elif punkty_gracza > 21:
            print("Przekroczyłeś 21! Przegrywasz.")
            return

        decyzja = input("Czy chcesz dobrać kartę? (t - tak, n - nie): ").lower()

        if decyzja == 't':
            reka_gracza.append(talia.pop())
        elif decyzja == 'n':
            koniec_gry = True
        else:
            print("Niepoprawna komenda. Wpisz 't' lub 'n'.")

    # TURA KRUPIERA
    punkty_krupiera = oblicz_punkty(reka_krupiera)
    print(f"\n--- RUCH KRUPIERA ---")
    print(f"Karty krupiera: {reka_krupiera} (Punkty: {punkty_krupiera})")

    # Krupier musi dobierać, jeśli ma mniej niż 17 punktów
    while punkty_krupiera < 17:
        print("Krupier dobiera kartę...")
        reka_krupiera.append(talia.pop())
        punkty_krupiera = oblicz_punkty(reka_krupiera)
        print(f"Karty krupiera: {reka_krupiera} (Punkty: {punkty_krupiera})")

    # SPRAWDZENIE WYNIKÓW
    punkty_gracza = oblicz_punkty(reka_gracza)

    print("\n=== WYNIKI ===")
    if punkty_krupiera > 21:
        print("Krupier przekroczył 21! Wygrywasz!")
    elif punkty_gracza > punkty_krupiera:
        print("Masz więcej punktów! Wygrywasz!")
    elif punkty_krupiera > punkty_gracza:
        print("Krupier ma więcej punktów. Przegrywasz.")
    else:
        print("Remis!")


# Uruchomienie programu
if __name__ == "__main__":
    zagraj_w_blackjacka()