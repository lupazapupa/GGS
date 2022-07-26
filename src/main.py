import random


class Wish:
    def __init__(self):
        self.five_star_characters = ["Venti", "Mona", "Qiqi", "Diluc", "Jean", "Keqing"]
        self.four_star_characters = ["Fischl", "Xiangling", "Barbara", "Beidou", "Bennett", "Chongyun", "Diona",
                                     "Gorou",
                                     "Kujou Sara", "Kuki Shinobu", "Ningguang", "Noelle", "Rasor", "Rosaria", "Sayu",
                                     "Shikanoin Heizou", "Sucrose", "Thoma", "Xingqiu", "Xinyan", "Yanfei", "Yun Jin"]
        self.four_star_weapons = ["Dragon's Bane", "Eye of Perception", "Favonius Lance", "Favonius Sword",
                                  "Favonius Codex",
                                  "Favonius Greatsword", "Favonius Warbow", "Lion's Roar", "Rainslasher", "The Bell",
                                  "The Flute", "The Stringless", "The Widsith", "Rust", "Sacrifical Bow",
                                  "Sacrifical Fragments", "Sacrifical Sword", "Sacrifical Greatsword"]
        self.three_star_weapons = ["Black Tassel", "Bloodtained Greatsword", "Cool Steel", "Debate Club",
                                   "Emerald Orb", "Ferrous Shadow", "Harbinger of Dawn", "Magic Guide", "Raven Bow",
                                   "Sharpshooter's Oath", "Skyrider Sword", "SlingShot",
                                   "Thrilling Tales of Dragon Slayers"]
        self.count = 0
        self.count10 = 0
        self.garant_Num_10 = 10
        self.garant_Num = 90
        self.gems = 160
        self.garant5 = False
        self.garant4 = False
        self.n = 0

    def wish(self, gems: int):
        character = ""
        if gems >= 160:
            self.count += 1
            self.count10 += 1
            if self.garant_Num == self.count and self.garant5:
                character = self.five_star_characters[0]
                self.garant5 = False
                self.garant4 = True
                self.count = 0
                self.count10 = 0
            elif self.garant_Num == self.count:
                choice = random.randint(1, 2)
                if choice == 1:
                    character = self.five_star_characters[0]
                    self.garant5 = False
                    self.garant4 = True
                    self.count = 0
                    self.count10 = 0
                elif choice == 2:
                    character = self.five_star_characters[random.randint(1, len(self.five_star_characters)-1)]
                    self.count = 0
                    self.count10 = 0
                    self.garant5 = True
                    self.garant4 = True
            elif self.count < self.garant_Num:
                if self.count10 == self.garant_Num_10 and self.garant4:
                    character = self.four_star_characters[random.randint(0, 2)]
                    self.garant4 = False
                    self.count10 = 0
                elif self.count10 == self.garant_Num_10:
                    choice = random.randint(1, 2)
                    if choice == 1:
                        character = self.four_star_characters[random.randint(0, 2)]
                        self.garant4 = False
                        self.count10 = 0
                    elif choice == 2:
                        character = random.choice(self.four_star_characters[3:] + self.four_star_weapons +
                                                  self.five_star_characters)
                        self.count10 = 0
                        self.garant4 = True
                        if character == self.five_star_characters[0]:
                            self.garant5 = False
                            self.count = 0
                        elif character in self.five_star_characters:
                            self.garant5 = True
                            self.count = 0
                else:
                    self.n = random.randint(0, 1000)
                    if 0 <= self.n <= 6:
                        character = random.choice(self.five_star_characters)
                        if character == self.five_star_characters[0]:
                            self.garant5 = False
                            self.garant4 = True
                            self.count = 0
                            self.count10 = 0
                        else:
                            self.garant5 = True
                            self.garant4 = True
                            self.count = 0
                            self.count10 = 0
                    elif 6 < self.n <= 57:
                        character = random.choice(self.four_star_characters + self.four_star_weapons)
                        if character == self.four_star_characters[0] or character == self.four_star_characters[1] or\
                                character == self.four_star_characters[2]:
                            self.garant4 = False
                            self.count10 = 0
                        else:
                            self.garant4 = True
                            self.count10 = 0
                    else:
                        character = random.choice(self.three_star_weapons)

        return character


def start():
    gems = 0
    inv = []
    wish = Wish()
    while True:
        command = input("Введите команду: ")
        commandlist = ['Баланс', 'Пополнить', 'Крутить', 'Инвентарь', 'Помощь', 'Выход']
        match command.strip():
            case "Баланс":
                print("На вашем счету {} примогемов: ".format(gems))
            case "Пополнить":
                gems += int(input("Введите необходимое для пополнения количество примогемов: "))
                print("На вашем счету {} примогемов: ".format(gems))
            case "Крутить":
                while True:
                    tries = int(input("Сколько раз вы хотите помолиться (1, 10 или 0 для выхода): "))
                    if gems >= 1600 and tries == 10:
                        for i in range(0, 10):
                            character = wish.wish(gems)
                            print(character)
                            if not(character in inv):
                                inv.append(character)
                        gems -= 1600
                        print("На вашем счету {} примогемов: ".format(gems))
                    elif gems >= 160 and tries == 1:
                        character = wish.wish(gems)
                        print(character)
                        if not (character in inv):
                            inv.append(character)
                        gems -= 160
                        print("На вашем счету {} примогемов: ".format(gems))
                    elif gems < 1600 and tries == 10:
                        print("Вам не хватает {} примагемов для совершения 10 молитв".format(1600-gems))
                    elif gems < 160 and tries == 1:
                        print("Вам не хватает {} примагемов для совершения молитвы".format(160-gems))
                    elif tries == 0:
                        break
            case "Помощь":
                print("Список доступных команд: ", commandlist)
            case "Выход":
                break
            case "Инвентарь":
                if len(inv) == 0:
                    print("У вас ничего не открыто")
                else:
                    print("Вы открыли: ", '\n'.join(inv))
            case _:
                print("Данная команда не существует. Попробуйте снова")


if __name__ == '__main__':
    print("Добро пожаловать в Геншин гачу!\nДля вывода доступных команд введите команду: Помощь")
    try:
        start()
    except KeyboardInterrupt:
        print("\nВы вышли")
    except EOFError:
        print("Вы вышли")
