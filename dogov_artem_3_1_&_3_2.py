# 1    Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# --------------Решение----------------------
# обьявляем функцию num_translate
def num_translate(num):
    # в нутри функции обьявляем словарь my_numbers
    my_numbers = {'zero': 'ноль',
                  'one': 'один',
                  'two': 'два',
                  'there': 'три',
                  'four': 'четыре',
                  'five': 'пять',
                  'six': 'шесть',
                  'seven': 'семь',
                  'eighth': 'восемь',
                  'nine': 'девять',
                  'ten': 'десять'}

    # проверяем наличие ключа в словаре
    if num in my_numbers:
        # Если есть то возвращем значение по ключу
        return my_numbers[num]
    else:
        # Если нет то возвращаем None
        return None


# Проверяем
print(num_translate('one4'), )


# 2  *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
# числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавно
# --------------Решение----------------------
# обьявляем функцию num_translate_adv


def num_translate_adv(num):
    # проверяем нулевой символ атрибута num
    if num[0].isupper():
        # если нулевой символ -заглавная буква, то вызываем функцию  num_translate и передаем ей параметром атрибут
        # num, только с маленькой буквы, полученый результат приравневаем к переменной res
        res = num_translate(num.lower())
        # почему нельзя использовать конструцию вида return num_translate(num.lower()).capitalize()
        # потому что если num_translate вернет None то метод capitalize не сработает и будет ошибка.
        # поэтому необходимо проверить что  вернула  функция num_translate
        if res is not None:
            #если результат не None, то возвращаем capitalize
            return res.capitalize()
        else:
            # а если все таки None, то и  возвращаем None
            return None
    else:
        # если нулевой символ - не заглавная буква, то вызываем функцию  num_translate и передаем ей параметром
        # атрибут и сарзу же его возвращаем
        return num_translate(num)

# Проверяем
print(num_translate_adv('seven'))
print(num_translate_adv('Five'))
