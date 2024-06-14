# guessing-game v0.2.4

import random



#asdf
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

        elif gues > num:
            print("zahl zu groß")

        elif gues < num:
            print("zahl zu klein")
    return highscore

#highscore = str(guessnumb())

def save_score(highscore):
    #speichert den highscore in einer datei ab
    #todo: implementieren sie diese funktion
    with open('score.txt', 'w') as f:
        f.write(str(highscore))






while True:
    highscore = guessnumb()

    correctinput = False
    while not correctinput:
        print("Wollen Sie das spiel neu starten? y/n")
        choice = input("Geben Sie y oder n ein.")
        if choice == "y":
            guessnumb()
        elif choice == "n":
            save_score(highscore)
            exit(0)
        else:
            print("falsch eingabe")







