# Введем наименования игроков и списки для учета их ходов
first_player_name = 'Крестик'
first_player_steps = []
second_player_name = 'Нолик'
second_player_steps = []

# Назначим игрока, который делает текущий ход
current_player = first_player_name

# Запишем в матрицу победные комбинации
# комбинация записывается двузначным числом:
# первое число означает номер строки, второе - номер колонки
winner_combinations = [
    ['00', '01', '02'],
    ['10', '11', '12'],
    ['20', '21', '22'],
    ['00', '10', '20'],
    ['01', '11', '21'],
    ['02', '12', '22'],
    ['00', '11', '22'],
    ['02', '11', '20'],
]

# Определяет и возвращает значение текущей ячейки
def current_cell(cell):

    # Присвоим ячейке значение по умолчанию
    cell_value = '-'

    # Проверяем, не заполнена ли данная ячейка крестиками
    if cell in first_player_steps:
        cell_value = 'x'
    # Если крестиками не заполнена - проверяем на нолики
    elif cell in second_player_steps:
        cell_value = 'o'

    return cell_value

# Строит игровое поле со сделаными игроками ходами
def players_field():

    print('')

    print('  0 1 2')
    for row in range(3):
        # не знаю, как в цикле вывести строку, потому что первой колонкой должен быть номер строки
        cell0, cell1, cell2 = str(row) + '0', str(row) + '1', str(row) + '2'
        print(str(row) +  ' ' + current_cell(cell0) + ' ' + current_cell(cell1)+  ' ' + current_cell(cell2))

    print('')

# Определяет, есть ли победитель и возвращает True если есть, иначе False
def win(player_steps):
    # Ищем по очереди все победные комбинации в ходах игрока
    for i in winner_combinations:
        maybe_win = True
        for j in i:
            if not j in player_steps:
                maybe_win = False
                break
        # нашли все ячейки победной комбинации в ходах игрока
        if maybe_win == True:
            break

    return maybe_win


print('Добро пожаловать в игру крестики-нолики!')
print('Правила игры:')
print('Для того,чтобы сделать ход, игрок должен ввести двузначное число,')
print('в котором первая цифра - это номер строки, в которую он хочет поставить знак,')
print('а вторая цифра - это номер колонки.')
print('Результат хода отображается на экране.')
print('')
print('Первым ходит игрок, играющий за крестики.')
print('')
print('ПОГНАЛИ!')



# Отобразим начальное игровое поле
players_field()

# Начинаем бесконечный цикл ходов, который закончится победой или ничьей
# Хотя максимальное количество ячеек известно - ходов может быть больше с учетом возможных ошибок ввода
while True:

    # запишем в переменную ход текущего игрока
    step = input('Ход игрока ' + current_player + ': ')

    # Проверим, корректно ли ввел игрок цифры
    if len(step) != 2:
        print('Цифр должно быть ровно две. Сделайте ход еще раз')
        continue

    for letter in step:
        wrong_num = False
        if int(letter) > 2:
            print('Цифры должны быть от 0 до 2. Сделайте ход еще раз')
            wrong_num = True
            break
    if wrong_num:
        continue

    # Проверим, не заполнено ли уже поле, в которое походил игрок, другим значением
    if step in first_player_steps or step in second_player_steps:
        print('Это поле уже занято. походите в другое, свободное поле')
        continue

    # Добавим ход в историю ходов этого игрока
    if current_player == first_player_name:
        first_player_steps.append(step)
    else:
        second_player_steps.append(step)

    # Отобразим игровое поле со всеми ходами
    players_field()

    # Проверим, победил ли текущий игрок. Если победил - сообщаем и выходим из цикла
    if win(first_player_steps if current_player == first_player_name else second_player_steps):
        print(f'Игра окончена. Победил игрок {current_player}')
        break

    # Проверим, не окончена ли игра
    # окончена, если сумма ходов обоих игроков равна 9 (на всякий случай возьмем >=)
    if len(first_player_steps) + len(second_player_steps) >= 9:
        print('Игра окончена. Результат: Боевая ничья!!!')
        break

    # Оснований заканчивать игру нет. Меняем текущего игрока и уходим на следующую итерацию
    current_player = first_player_name if current_player == second_player_name else second_player_name