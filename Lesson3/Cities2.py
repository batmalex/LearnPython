def check_city(city):
    return len(city) > 0 and city[0].isalpha() and city[-1].isalpha()


def get_last_letter(city):
    i = 1
    while (city[-i].lower() in 'ьъы' and i <= len(city)) or not city[-i].isalpha():
        i += 1
    letter = city[-i].lower()
    if letter == 'ё':
        letter = 'е'
    elif letter == 'й':
        letter = 'и'
    return letter


def user_city(letter):
    result = None
    while True:
        city = input('Введите город на букву {}: '.format(letter.upper())).lower()
        if not check_city(city):
            continue
        if letter == city[0]:
            # Если буква в справочнике не определена, то создаем пустой справочник и город
            if cities.get(letter, 0) == 0:
                cities[letter] = {}
            found_city = cities[letter].get(city, 2)
            # Если город уже использовался
            if found_city == 1:
                print("Уже называли")
            # Город не использовался
            else:
                if found_city == 0:
                    pass
                    # print("Город {0} найден".format(city))
                elif found_city == 2:
                    print("Ммм.., допустим есть такой город")
                cities[letter][city] = 1
                result = get_last_letter(city)
                break
        elif city == "q":
            break
    return result


def bot_city(letter):
    result = None
    if cities.get(letter, 0) == 0:
        cities[letter] = {}
        print("Я не знаю городов на букву {}".format(letter.upper()))
    else:
        for city, value in cities[letter].items():
            # print(key, value)
            if value == 0:
                print(city.capitalize())
                cities[letter][city] = 1
                result = get_last_letter(city)
                break
        else:
            print("Я не знаю больше городов на букву {}".format(letter.upper()))
    return result


def load_cities(file_path):
    with open(file_path) as cities_from_file:
        for city in cities_from_file:
            city = city.lower().rstrip()
            letter = city[0]
            if cities.get(letter, 1) == 1:
                cities[letter] = {}
            if cities[letter].get(city, 1) == 1:
                cities[letter][city] = 0
        # new_cities = {{city: 0} for city in cities}
        # print(cities)


def city_game():
    load_cities(file)
    letter = 'м'
    letter = bot_city(letter)
    while letter:
        letter = user_city(letter)
        if letter:
            letter = bot_city(letter)


file = './cities.txt'
cities = {}
city_game()
# cities = {'а': {'Ашхабад': 0, 'Алматыб': 0, 'Ангарска': 0}, 'б': {'Барнаула': 0, 'Братск': 0}, 'д': {'Дублин': 0}, 'м': {'Мокровка': 0}, 'н': {'Новосиб': 0}, 's': {}}




