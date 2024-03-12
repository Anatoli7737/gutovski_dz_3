# Anatoli Gutovski
# Date: 05/03/2024
# Description: Homework 3
# Grodno IT Academy Python 3.11.7


# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: `1 1 1` - это 3 пары, `1 1 1 1` - это 6 пар.

def pairs(numbers):
    # Разделяем строку на список чисел
    numbers = numbers.split()
    # Задаем начальное значение переменной
    pairs = 0
    # Проходим по индексам списка чисел
    for i in range(len(numbers)):
        # Проходим по индексам, начиная с i+1, чтобы не учитывать повторные пары
        for j in range(i+1, len(numbers)):
            # Если числа на позициях i и j равны
            if numbers[i] == numbers[j]:
                # Увеличиваем счетчик пар
                pairs += 1
    # Возвращаем количество найденных пар
    return pairs
    # Рабочее решение, для интереса см ответы для решения без вложенных циклов


# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

def uniques(array):
    # Создадим пустой списой, в который будут добавляться уникальные элементы
    uniques = []
    # Создадим пустое множество, которое будет содержать элементы, встречающиеся более одного раза
    replays = set()
    for i in array:
        # Проверка, что текущий элемент i не встречается в множестве replays
        if i not in replays:
            # Проверка, что текущий элемент i уже есть в списке uniques
            if i in uniques:
                # Удалим элемент i из списка uniques, так как он встретился повторно
                uniques.remove(i)
                # Добавим элемент i в множество replays, чтобы отметить его как повторяющийся
                replays.add(i)
            else:
                # Иначе добавляем текущий элемент i в список uniques, так как он уникален
                uniques.append(i)
    return uniques
    # Тоже рабочий вариант, но можно сильно сократить код, просто проверяя, что элемент встречается один раз. см ответы

# Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
# дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
# Верните полученный список.
# Задача не проходит тест. Такой вариант решения мог бы быть, но всего с одним исправлением - item == 0 (см ответы)

def ordered_list(array):
    # Пройдемся по списку в обратном порядке
    for i in reversed(range(len(array))):
        # Если текущий элемент равен нулю, перемещаем его в конец списка
        if array[i] == 0:
            # Это условие проверяет, является ли текущий элемент списка равным нулю
            array.append(array.pop(i))
    return array
    # Тут много вариантов решения, можно проще, см ответы


# Возмите кортеж `('a', 'b', 'c')`, И сделайте из него список.

def tuple_to_list(in_tuple):
    # Преобразование кортежа в список с помощью функции list()
    lst = list(in_tuple)
    return lst
    # Верно


# Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию). can't call itself

def euclid(a, b):
    # Это цикл while, который будет выполняться, пока b не станет равным нулю.
    while b:
        # Мы присваиваем новое значение b переменной a, а новое значение a % b переменной b.
        a, b = b, a % b
    return a
    # Верно


# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
# Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции).
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.
# Пример данных:
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod
# Выходные данные
# Ukraine
# Russia
# Russia
# input_string = "2\nRussia Moscow Petersburg Novgorod Kaluga\nUkraine Kiev Donetsk Odessa\n3\nOdessa\nMoscow\nNovgorod"
# output_string = 'Ukraine\nRussia\nRussia'
# country_map={}

def cities(input_string):
    # Cоздадим пустой словарь, в котором будут храниться соответствия городов и стран
    countries = {}
    # Никаких инпутов в домашних заданиях! Это количество нужно получить из строки.
    # Ввод количества стран и их городов
    N = int(input())
    for _ in range(N):
        # Считывание строки, содержащей название страны и список городов, разделенных пробелами
        country, *cities = input().split()
        # Цикл для перебора каждого города в списке городов
        for city in cities:
            countries[city] = country

    # Ввод количества запросов
    M = int(input())

    # Обработка запросов
    input_string = ""
    for _ in range(M):
        city = input()
        # Проверка, является ли город "Brest"
        if city == "Brest":
            input_string += "Belarus France\n"
        else:
            # Получение значения из словаря countries по ключу city
            country = countries.get(
                city, "Город не входит в перечисленные выше города")
        input_string += country + "\n"

    return input_string
    # Решение неверное, разберем на занятии, см ответы


# Задачи для домашней работы
# Языки
# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
# Пример входных данных:
# 3 # N количество школьников
# 2 # M1 количество языков первого школьника
# Russian # языки первого школьника
# English
# 3 # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
# input_string = "3\n2\nRussian\nEnglish\n3\nRussian\nBelarusian\nEnglish\n3\nRussian\nItalian\nFrench"
# output_string = '1\nRussian\n5\nRussian\nFrench\nItalian\nEnglish\nBelarusian'

def languages(input_string):
    # Преобразуем входную строку в число n - количество школьников
    # Никаких инпутов в домашних заданиях! Это количество нужно получить из строки.
    n = int(input())
    # Создадим список languages_sets, содержащий n пустых множеств для хранения языков каждого школьника
    languages_sets = [set() for _ in range(n)]

    for i in range(n):
        # Считывание числа m, представляющего количество языков, которые знает текущий школьник
        # Никаких инпутов в домашних заданиях! Это количество нужно получить из строки.
        m = int(input())
        for _ in range(m):
            # Добавим считанные языки в множество языков текущего школьника
            languages_sets[i].add(input())

    # Найдем пересечения всех множеств языков (языки, которые знают все школьники)
    all_languages = set.intersection(*languages_sets)
    # Найдем объединения всех множеств языков (все уникальные языки, которые знают хотя бы один школьник)
    any_languages = set.union(*languages_sets)

    # Создадим пустой списой для хранения результата
    result = []
    # Добавление в результат количество языков в пересечении
    result.append(len(all_languages))
    # Добавление в результат отсортированных языков из пересечения
    result.extend(sorted(all_languages))
    # Добавление в результат количество всех уникальных языков
    result.append(len(any_languages))
    # Добавление в результат отсортированных всех уникальных языков
    result.extend(sorted(any_languages))
    # Форматирование строки результата с добавлением кавычек и запятых
    # Это не нужно
    input_string = "[" + \
        ", ".join(map(lambda x: "'" + str(x) + "'", result)) + "]"
    return input_string
    # Логика решения практически верна, инпуты ломают выполнение


# Generators

# Генераторы списков
# Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']. из ['x','y'] & ['y','z','v']

def list_gen(arr1, arr2):
    # Cоздаем список, содержащий суммы всех пар элементов из arr1 и arr2
    result = [i+j for i in arr1 for j in arr2]
    return result
    # Верно


# Генераторы словарей

# Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до N, а значениями кубы этих чисел.

def dict_gen(N):
    # Cоздадим словарь, где ключи — числа от 1 до N, а значения — их кубы.
    result = {i: i**3 for i in range(1, N+1)}
    return result
    # Верно


# Кортежи

# Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.

def multiplication_table(N):
    # В этой строке создается генератор, который заполняет каждую ячейку таблицы умножения произведением двух чисел i и j
    table = ((f'{i*j:>{len(str(N*N))}}' for i in range(N+1))
             for j in range(N+1))
    # Здесь создается генератор, который объединяет элементы в каждой строке таблицы через пробел
    table_gen = (' '.join(row) for row in table)
    table = table_gen
    return table
# Рабочее решение, хотя ожидалось, что это будет функция-генератор с yield. Но тесты проходятся
