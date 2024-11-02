# Игровое поле
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Победные комбинации, указаны индексы позиций
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]
# Вывод игрового поля на экран
def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

# Отмечаем ход Х или О в зависимости от указанного игроком числа
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
# Проверяем, нет ли выигрышной комбинации
def get_result():
    win = ""
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
    return win

# Игра
game_over = False
player1 = True

while game_over == False:

    # Вывод игрового поля
    print_maps()

    # Запрос хода
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, Ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, Ваш ход: "))
    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определяем победителя
    if win != "":
            game_over = True
    else:
            game_over = False

    player1 = not(player1)

# Вывод на экран результатов игрового поля и победителя
print_maps()
print("Победил", win)