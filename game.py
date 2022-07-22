from random import randint

difficulty_str = input("Wybierz poziom trudności (1 - łatwy, 2 średni, 3 - trudny): ")
difficulty = int(difficulty_str)

if difficulty == 1:
    print("Zgadnij liczbę od 1 do 20")
    answer = randint(1, 20)
elif difficulty == 2:
    print("Zgadnij liczbę od 1 do 50")
    answer = randint(1, 50)
elif difficulty == 3:
    print("Zgadnij liczbę od 1 do 100")
    answer = randint(1, 100)
else:
    print("Nieprawidłowy poziom trudności!")

guess_as_string = input("Podaj liczbę: ")
guess = int(guess_as_string)
i = 1

while guess != answer:
    i = i + 1
    if guess < answer:
        print("Za mało!")
    else:
        print("Za dużo!")
    i_str = str(i)
    print("Próba " + i_str)
    guess_as_string = input("Podaj liczbę: ")
    guess = int(guess_as_string)

print("Ukończyłeś w " + i_str + ". podejściu. Gratulacje!")