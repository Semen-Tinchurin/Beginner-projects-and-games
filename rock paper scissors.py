import random
while True:
    user_action = input('Сделай выбор - камень, ножницы или бумага: ')
    possible_actions = ['камень', 'ножницы', 'бумага']
    comp_action = random.choice(possible_actions)
    print(f"\n Ты выбрал {user_action}, комп выбрал {comp_action}.\n")
    if user_action == comp_action:
        print(f"Оба выбрали {user_action}. Ничья")
    elif user_action == "камень":
        if comp_action == "ножницы":
            print("камень бьет ножницы, ты выиграл")
        else:
            print("бумага оборачивает камень, ты проиграл")
    elif user_action == "бумага":
        if comp_action == 'камень':
            print("бумага оборачивает камень, ты выиграл")
        else:
            print("ножницы режут бумагу, ты проиграл")
    elif user_action == "ножницы":
        if comp_action == "бумага":
            print("ножницы режут бумагу, ты выиграл")
        else:
            print("камень бьет ножницы, ты проиграл")
    play_again = ''
    play_again = input("сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break