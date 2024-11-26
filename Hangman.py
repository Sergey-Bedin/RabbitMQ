import random

words_list = [
    "factor",
    "pilot",
    "battle",
    "nirvana",
    "shit",
    "uncle",
    "bang",
    "ramp",
    "dust",
    "note",
    "game",
    "task",
    "mission",
]
for i in range(len(words_list)):
    words_list[i] = words_list[i].upper()

#print(words_list)


def get_word(words_list):
    return random.choice(words_list)


def display_hangman(tries):

    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def play(word):
    word_completion = "_" * len(word)
    flag_game = True  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    print("Давай сыграем в угадайку слов")
    test = input().upper()
    while flag_game:
        while not word_completion.isalpha():
            if not test.isalpha():
                print("НЕ пон, введи букву или слово целиком!")
                test = input().upper()
            elif test in guessed_letters:
                print("Ты уже называл эту букву")
                test = input().upper()
                continue
            elif test in guessed_words:
                print("Ты уже называл это слово")
                test = input().upper()
                continue
            elif test.isalpha():
                guessed_letters.append(test)
                guessed_words.append(test)
                if test in word and len(test) == 1:
                    for i in range(len(word)):
                        if test == word[i]:
                            word_completion = (word_completion[: i] + test + word_completion[i + 1 :])
                    print(word_completion)
                    if word_completion == word:
                        print("Хорош, ты выиграл")
                        break
                elif test == word:
                    word_completion = test
                    break
                else:
                    tries -= 1
                    if tries > 0:
                        print("Смерть близко...")
                        print("Попыток осталось:", tries)
                        print(display_hangman(tries))
                        print(word_completion)
                    else:
                        break
                test = input().upper()
        if tries == 0:
            print("Сори, ты проиграл(")
            print(display_hangman(tries))
            break
        elif test == word:
                print("Хорош, ты выиграл")
                break


guess = get_word(words_list)
#print(guess)
play(guess)
