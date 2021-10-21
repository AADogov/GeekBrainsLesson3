# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
# списков (по одному из каждого):
# --------------Решение----------------------
# импортируем модуль random
import random


# обьявляем функцию get_jokes и документацию к ней
def get_jokes(n: int = 1, flag: bool = True):
    """
    Function that returns n jokes formed from three random words taken from three lists
    (one from each when flag is true)
    :param n: number of jokes that need to be return, default n=1
    :param flag: that allows (true) or prohibits (false) repetition of words in jokes, default flag = True
    :return: result string
    """
    # обьявляем 3 исходных списка nouns; adverbs; adjectives;
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "гладкий"]
    # обьявляем переменную result для результата
    result = ""
    # запускаем цикл от 0 до n
    for i in range(0, n):
        # обьявляем 3 переменые которые будут составлять шутку выбираем их случайным образм из каждого из 3 списком
        # случайным образом методом random.choice
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        if not flag:
            # Если flag = false
            # тогда проверяем что в каждом из 3 списков имеется по крайней мере 1 элемент
            if len(nouns) > 1 and len(adverbs) > 1 and len(adjectives) > 1:
                # и удаляем из списков по 1 выбранному элементу, таким образом исключив повторения в будующем
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)
            else:
                # в случае когда хотя бы в одном из списков остлся 1 элемент мы добавляем в результат наши выбранные
                # слова и добавляем фразу "Шутки кончились" и прекращаем цикл.
                result += f'{noun} {adverb} {adjective};   '
                result += "Шутки кончились"
                break
        # Если flag = True мы добавляем в результат наши выбранные слова и переходим к следующей итерации
        result += f'{noun} {adverb} {adjective};   '
    # По завершению цикла возвращаем результат
    return result


# Проверяем
print(get_jokes(8, False))
print(get_jokes(8))
