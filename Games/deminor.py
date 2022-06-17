import random

nb_col = 11
nb_line = 11
list_character = [0, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
list_bombs = []
list_chosen = []
dict_level = {
    "Easy": 15,
    "Medium": 30,
    "Hard": 60,
    "Master": 90
}


def get_table():
    tab = [[0] * nb_col for _ in range(nb_line)]
    for i in range(nb_line):
        tab[0][i] = i - 1
        tab[i][0] = list_character[i]
    return tab


def print_table(tab):
    for i in range(nb_col):
        for j in range(nb_line):
            if (j - 1, list_character[i]) in list_chosen:
                print("  ", end='')
                continue
            elif tab[i][j]:
                print(str(tab[i][j]) + " ", end='')
            else:
                print("0 ", end='')
        print("\n", end='')


def set_bombs(number_of_bomb):
    while number_of_bomb > 0:
        ran_col = random.randint(0, 9)
        ran_line = random.choice(list_character)
        if (ran_col, ran_line) not in list_bombs and ran_line != 0:
            list_bombs.append((ran_col, ran_line))
            number_of_bomb -= 1


def check_position(column, Line):
    good = True
    if column > 10 or column < 0:
        good = False
    if Line not in list_character:
        good = False
    return good


def get_level():
    while True:
        level = input("Choose a level (Easy / Medium / Hard / Master ): ")
        if level in dict_level.keys():
            break;
    return level


tab = get_table()
set_bombs(dict_level.get(get_level()))

while True:
    print_table(tab)
    col = int(input("choose a col : "))
    line = input("choose a line : ")
    if not check_position(col, line):
        print("Bad column or line number")
        continue
    if (col, line) in list_chosen:
        print("you have selected this case")
        continue
    if (col, line) in list_bombs:
        print("You lose")
        break
    list_chosen.append((col, line))
