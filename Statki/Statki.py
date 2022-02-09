import random
import os


collumn_names = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}

i = 0
u = 12
v = 12
# Naprawić wypierdalanie się programu gdy plansza ma wymiary 11 x 11
user_life = 50
size = 0
shots = []
hits = 0
message = ''

list_of_ships = [[]for x in range(5)]
ship_number = 0

map = [['-' for x in range(u)] for y in range(v)]
map[0] = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
x = 1
while x < 11:
    map[x][0] = x
    x += 1

user_map = [['-' for x in range(u)] for y in range(v)]
user_map[0] = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
x = 1
while x < 11:
    user_map[x][0] = x
    x += 1

print('Witaj w grze w statki')
print('Ilość statków w grze:')
print('1 statek - 4 pola')
print('2 statki - 3 pola')
print('2 statki - 2 pola')
print('Masz ', user_life, ' żyć')

# Czyszczenie okna
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# FINKCJA ROZMIESZCZAJĄCA STATKI NA MAPIE
def add_ship(size, ship_number):


    direction = random.randint(0, 1)

    # FORSOWANIE KIERUNKU
    # direction = 1


    if direction == 0:
        row = random.randint(1, 7)
        col = random.randint(1, 10)
    if direction == 1:
        row = random.randint(1, 10)
        col = random.randint(1, 7)

    # PIONOWO
    if direction == 0:
        # print('0 - pionowo')
        # print('row = ' + str(row))
        # print('col = ' + str(col))

        #     # SPRAWDZANIE KOLIZJI
        i = 0
        collision = 0
        while i < size + 2:

            if map[row + i - 1][col] == 'X':
                # print('kolizja1')
                collision = 1
                return 1
                break
            if map[row + i - 1][col] == 'o':
                # print('kolizja2')
                collision = 1
                return 1
                break
            i += 1

        if collision == 0:
            i = 0
            # pudła przed statkiem
            if row > 1:
                map[row - 1][col] = 'o'
                if col < 10:
                    map[row - 1][col + 1] = 'o'
                if col > 1:
                    map[row - 1][col - 1] = 'o'
            # statek plus pudla obok
            while i < size:
                map[row + i][col] = 'X'
                if col < 10:
                    map[row + i][col + 1] = 'o'
                if col > 1:
                    map[row + i][col - 1] = 'o'
                # Tutaj zapisywanie pozycji statku
                list_of_ships[ship_number].append([row + i, col])
                i += 1

            # pudła za statkiem
            if row + i < 11:
                map[row + i][col] = 'o'
                if col < 10:
                    map[row + i][col + 1] = 'o'
                if col > 1:
                    map[row + i][col - 1] = 'o'


    # POZIOMO
    else:
        # print('1 - poziomo')
        # print('row = ' + str(row))
        # print('col = ' + str(col))

        #     # SPRAWDZANIE KOLIZJI
        i = 0
        collision = 0
        while i < size + 2:

            if map[row][col + i - 1] == 'X':
                # print('kolizja1')
                collision = 1
                return 1
                break
            if map[row][col + i - 1] == 'o':
                # print('kolizja2')
                collision = 1
                return 1
                break
            i += 1

        if collision == 0:
            i = 0
            # pudła przed statkiem
            if col > 1:
                map[row][col - 1] = 'o'
                if row < 10:
                    map[row + 1][col - 1] = 'o'
                if row > 1:
                    map[row - 1][col - 1] = 'o'

            # statek plus pudla obok
            while i < size:
                map[row][col + i] = 'X'
                if row < 10:
                    map[row + 1][col + i] = 'o'
                if row > 1:
                    map[row - 1][col + i] = 'o'
                # Tutaj zapisywanie pozycji statku
                list_of_ships[ship_number].append([row, col + i])
                i += 1

            # pudła za statkiem
            if col + i < 11:
                map[row][col + i] = 'o'
                if row < 10:
                    map[row + 1][col + i] = 'o'
                if row > 1:
                    map[row - 1][col + i] = 'o'


    ship_number += 1
    # print(list_of_ships)
    return 0



# map[1][1] = 'TEST'
#
# while i < 11:
#     print(tab[i])
#     i += 1


# FUNKCJA SPRAWDZAJĄCA ZATOPIENIE
def ship_sunk(ship_number):

    row_check = 0
    col_check = 0
    pos_value = 0
    ship_len = len(list_of_ships[ship_number])
    i = 0
    ship_positions = list_of_ships[ship_number]
    # print(ship_positions)
    sunk = 0

    while i < ship_len:
        row_check = ship_positions[i][0]
        col_check = ship_positions[i][1]
        x = 0
        # print(row_check)
        # print(col_check)
        # print('.')

        pos_value = str(user_map[row_check][col_check])
        # print(pos_value)
        if pos_value != 'X':
            sunk = 1
        i += 1
    # print('koniec funkcji')
    if sunk == 0:
        message = 'ZATOPIONY!'
        # TU WPISAĆ FUNKCJĘ KTÓRA OPISZE STATEK DOOKOŁA PUDŁAMI

        n = 0
        while n < ship_len:
            user_map[list_of_ships[ship_number][n][0] - 1][list_of_ships[ship_number][n][1] - 1] = 'o'
            user_map[list_of_ships[ship_number][n][0] - 1][list_of_ships[ship_number][n][1]] = 'o'
            user_map[list_of_ships[ship_number][n][0] - 1][list_of_ships[ship_number][n][1] + 1] = 'o'
            user_map[list_of_ships[ship_number][n][0]][list_of_ships[ship_number][n][1] - 1] = 'o'
            user_map[list_of_ships[ship_number][n][0]][list_of_ships[ship_number][n][1]] = 'o'
            user_map[list_of_ships[ship_number][n][0]][list_of_ships[ship_number][n][1] + 1] = 'o'
            user_map[list_of_ships[ship_number][n][0] + 1][list_of_ships[ship_number][n][1] - 1] = 'o'
            user_map[list_of_ships[ship_number][n][0] + 1][list_of_ships[ship_number][n][1]] = 'o'
            user_map[list_of_ships[ship_number][n][0] + 1][list_of_ships[ship_number][n][1] + 1] = 'o'
            n += 1

        n = 0
        while n < ship_len:
            user_map[list_of_ships[ship_number][n][0]][list_of_ships[ship_number][n][1]] = 'X'

            n += 1




        # dopisywanie do mapy
        x = 1
        while x < 11:
            user_map[x][0] = x
            x += 1
        user_map[0] = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        # TU KONIEC FUNKCJI

        list_of_ships[ship_number] = [[0, 0] for x in range(ship_len)]
        # print(list_of_ships[ship_number])





collision = 1
while add_ship(4, 0) == 1:
    collision = 1
while add_ship(3, 1) == 1:
    collision = 1
while add_ship(3, 2) == 1:
    collision = 1
while add_ship(2, 3) == 1:
    collision = 1
while add_ship(2, 4) == 1:
    collision = 1


#  ZMIENIC WYSWIETLANIE PLANSZY!!!!!!!!!!!!!!!!!!!!!!
# i = 0
# while i < 11:
#     print(map[i])
#     i += 1


while True:
    clearConsole()

    print()
    print('Witaj w grze w statki')
    print('Ilość statków w grze:')
    print('1 statek - 4 pola')
    print('2 statki - 3 pola')
    print('2 statki - 2 pola')
    print('Masz ', user_life, ' żyć')


    i = 0
    while i < 11:
        print(user_map[i][0: 11])
        i += 1
    input_error = 0

    print(message)

    shot = input('Wprowadź pole strzału (najpierw kolumna): ')
    shotlist = list(shot)
    # print(shotlist[0])
    try:
        shot_col = shotlist[0]
        shot_row = shotlist[1]
        if len(shotlist) > 2:
            shot_row = shotlist[1] + shotlist[2]
    except:
        message = 'Podałeś błędne położenie'
        pass

# ZABEZPIECZENIA WPISANIA
    isdigit = 0
    if str.isdigit(shot_row):
        isdigit = 1
    if isdigit == 0:
        message = 'Podałeś zły numer wiersza'
        input_error = 1
    if isdigit == 1:
        if int(shot_row) == 0:
            message = 'Podałeś zły numer wiersza'
            input_error = 1
        if int(shot_row) > 10:
            message = 'Podałeś zły numer wiersza'
            input_error = 1
        if shot_col not in collumn_names:
            message = 'Podałeś złą nazwę kolumny'
            input_error = 1
        if len(shotlist) > 3:
            message = 'Wpisałeś zbyt dużo znaków'
            input_error = 1
        if shot in shots:
            message = 'Wpisałeś ponownie tą samą pozycję'
            input_error = 1

        shots.append(shot)

        if input_error == 0:
            collumn_number = int(collumn_names[shot_col])
            row_number = int(shot_row)


            if map[row_number][collumn_number] == '-':
                user_map[row_number][collumn_number] = 'o'
                user_life -= 1
                message = 'Pudło! Pozostało Ci ', user_life, ' żyć'

            if map[row_number][collumn_number] == 'o':
                user_map[row_number][collumn_number] = 'o'
                user_life -= 1
                message = 'Pudło! Pozostało Ci ', user_life, ' żyć'

            if map[row_number][collumn_number] == 'X':
                user_map[row_number][collumn_number] = 'X'
                hits += 1
                message = 'Trafiony!'

            if user_life == 0:
                message = 'Skończyły Ci się życia! \n', '  _____GAME OVER_____  '
                input('Wciśniej dowolny klawisz')
                break

            if hits == 14:
                message = 'Zestrzeliłeś wszystkie statki\n', '            WYGRAŁEŚ         '
                i = 0
                while i < 11:
                    print(user_map[i][0: 11])
                    i += 1
                input('Wciśnij dowolny klawisz')
                break


            # print(list_of_ships)
            # print('pierwsze pole to: ' + str(list_of_ships[0][0]))

#   Sprawdzanie zatopienia statku
            ship_sunk(0)
            ship_sunk(1)
            ship_sunk(2)
            ship_sunk(3)
            ship_sunk(4)

