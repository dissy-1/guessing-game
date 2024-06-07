# guessing-game v0.2.4

import random


def guessnumb():
    num = random.randrange(0, 100)
    print(num)
    fehler = True
    highscore = 0
    while fehler:       # while not fehler: // while fehler =! True:
        highscore += 1  # kurzform für : anzahl = anzahl + 1
        try:
            gues = int(input("welche zahl ist es zwischen 0 und 100? "))
            if gues < 0 or gues > 100:
                raise ValueError
        except ValueError:
            print("falsche eingabe")
            continue


        if gues == num:
            print(f"Richtig die gesuchte Zahl ist: {num}")
            print(f"Dein Score ist : {highscore} Versuch/e")
            fehler = False
            return True

        elif gues > num:
            print("zahl zu groß")
            fehler = True

        elif gues < num:
            print("zahl zu klein")
            fehler = True
    return False

guessnumb()

while True:

    correctinput = False
    while not correctinput:
        print("Wollen Sie das spiel neu starten? JA/NEIN")
        choice = input("Geben Sie JA oder NEIN ein.")
        if choice == "JA":
            guessnumb()
        elif choice == "NEIN":
            exit(0)
        else:
            print("falsch eingabe")





