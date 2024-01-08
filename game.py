import random

coins = 100  # Начальное количество монет у пользователя
most_expensive_gun = None  # Самая дорогая оружейная покупка
most_expensive_knife = None  # Самая дорогая покупка ножа

# Шансы победы при использовании разного оружия
weapon_chances = {'АК-47': 0.2, 'Патриот': 0.15}
knife_chances = {'Керамбит': 0.05, 'Нож бабочка': 0.1, 'Нож штык': 0.02}

def update_weapon_chances():
    global weapon_chances
    if most_expensive_gun == 'АК-47':
        weapon_chances['АК-47'] = 0.5
    if most_expensive_gun == 'Патриот':
        weapon_chances['Патриот'] = 0.4

def update_knife_chances():
    global knife_chances
    if most_expensive_knife == 'Керамбит':
        knife_chances['Керамбит'] = 0.08
    if most_expensive_knife == 'Нож бабочка':
        knife_chances['Нож бабочка'] = 0.15
    if most_expensive_knife == 'Нож штык':
        knife_chances['Нож штык'] = 0.03

def play_game(coins):
    print("Старт игры! Отбивайтесь от зомби!")
    result = random.choice([0, 1])  # 1 - победа, 0 - поражение
    if result == 1:
        jackpot = random.random()  # шанс на джекпот
        if jackpot < 0.05:  # 5% шанс на джекпот
            print("Поздравляем! Вы выиграли джекпот - 100 монет!")
            coins += 100
        else:
            winnings = random.randint(30, 50)  # случайный выигрыш от 30 до 50 монет
            print(f"Поздравляем! Вы выиграли {winnings} монет!")
            coins += winnings
    else:
        print("К сожалению, вы проиграли.")
    return coins

while True:
    choice = input('напишите опцию: информация/магазин/играть: ')
    if choice == 'информация':
        choice2 = input('!это бета тест! В магазине можно купишь пушки,ножи,патроны. Чем дороже пушка и нож тем больше % на победу. На кнопку играть начинается игра: отбиваетесь против зомби. напишите /назад/ чтобы вернуться: ')
        if choice2 == 'назад':
            continue  

    elif choice == 'магазин':
        print(f'У вас {coins} монет')
        choice3 = input('напишите опцию пушки/ножи/патроны/назад: ')
        if choice3 == 'пушки':
            guns = {'АК-47': 5000, 'Патриот': 2000}
            print('Доступные пушки в магазине:')
            for gun, price in guns.items():
                print(f'{gun}: {price} монет')
            purchase = input('Какое оружие вы хотите купить? ')
            if purchase in guns and coins >= guns[purchase] and (most_expensive_gun is None or guns[purchase] > guns[most_expensive_gun]): 
                most_expensive_gun = purchase
                update_weapon_chances()
                coins -= guns[purchase]
                print(f'Вы приобрели {purchase}')

        elif choice3 == 'ножи':
            knives = {'Керамбит': 700, 'Нож бабочка': 1000, 'Нож штык': 200}
            print('Доступные ножи в магазине:')
            for knife, price in knives.items():
                print(f'{knife}: {price} монет')
            purchase = input('Какой нож вы хотите купить? ')
            if purchase in knives and coins >= knives[purchase] and (most_expensive_knife is None or knives[purchase] > knives[most_expensive_knife]):
                most_expensive_knife = purchase
                update_knife_chances()
                coins -= knives[purchase]
                print(f'Вы приобрели {purchase}')

        elif choice3 == 'патроны':
            bullets = {'Патроны для АК-47': 70, 'Патроны для Патриота': 60}
            print('Доступные патроны в магазине:')
            for bullet, price in bullets.items():
                print(f'{bullet}: {price} монет')
            purchase = input('Какие патроны вы хотите купить? ')
            if purchase in bullets and coins >= bullets[purchase]:
                coins -= bullets[purchase]
                print(f'Вы приобрели {purchase}')

        elif choice3 == 'назад':
            continue  

    elif choice == 'играть':
        coins = play_game(coins)  
        print(f"Ваш баланс: {coins} монет")
    else:
        print("Пожалуйста, выберите корректную опцию.")
