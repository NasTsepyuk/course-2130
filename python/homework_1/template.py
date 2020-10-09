"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    return (number + 20 - number % 20 if number % 20 != 0 else number)


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    return (' '.join([word[::-1] for word in string.split()]))


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    return '; '.join(f'{key}: {value}' for key, value in dictionary.items())



def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    return sub_string[::-1] in string


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    result = []
    for string in strings:
        try:
            x, y, z, proizv = [int(i) for i in string.split()]
            if f'{x} {y} {z} {x * y * z}' == string and x * y * z >= 0:
                result += [string]
        except:
            pass
    return result


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    for j in string:
        if j == '#':
            string.find('#')
            string = string[:string.find('#') - 1] + string[string.find('#') + 1:]
    string = string.replace('#', '')
    return string


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    uniq_sum = 0
    for i in lst:
        if lst.count(i) == 1:
            uniq_sum += i
    return uniq_sum


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    import re
    s = re.findall(r'\d+', string)
    for i in range(len(s)):
        s[i] = int(s[i])
    return max(s)


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    return '0' * (5 - len(str(number))) + str(number)


def t10(string):
    """
    Произведите смешивание цветов. Вам будет дана строка, необходимо смешать все пары цветов и вернуть результируюший
        цвет

    Комбинации цветов:    G G     B G    R G   B R
    Результирующий цвет:   G       R      B     G

    R R G B R G B B  <- ввод
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G  <-- вывод

    """
    string = [x for x in string]

    colors = ['B', 'G', 'R']

    while len(string) != 1:
        for i in range(len(string) - 1):
            if string[i] != string[i + 1]:
                string[i] = [x for x in colors if x not in string[i:i + 2]][0]
        string.pop()
    return string[0]


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    index = -1
    for i in range(len(lst)):
        if sum(x for x in lst[0:i]) == sum(x for x in lst[i + 1::]):
            index = i
            break
    return index


def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    import re
    numbers = []
    numbers_upd = []
    for i in lst:
        numbers += re.findall(r'[\+]?[78]?[\s(-]?\d{3}[\s' ')-]?\d{3}[\s' ')-]?[\s]?\d{2}[' ')-]?\d{2}[' ')-]?', i)
    for j in numbers:
        j = j.replace('+7', '8').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
        numbers_upd += [j]
    return numbers_upd


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    result = ''
    if len(str(number_1)) > len(str(number_2)):
        number_2 = '0' * (len(str(number_1)) - len(str(number_2))) + str(number_2)
    else:
        number_1 = '0' * (len(str(number_2)) - len(str(number_1))) + str(number_1)
    for i, j in zip(str(number_1), str(number_2)):
        result += str(int(i) + int(j))
    return int(result)


def t14(string):
    """
    Преобразуйте математическое выражение (символьное) в буквенное выраэение

    Для операций используйте следующую таблицу
        { '+':   'Plus ',
          '-':   'Minus ',
          '*':   'Times ',
          '/':   'Divided By ',
          '**':  'To The Power Of ',
          '=':   'Equals ',
          '!=':  'Does Not Equal ' }
    Примеры:
        4 ** 9 -> Four To The Power Of Nine
        10 - 5 -> Ten Minus Five
        2 = 2  -> Two Equals Two
    """
    changed_value = {'+': 'Plus ',
                     '-': 'Minus ',
                     '*': 'Times ',
                     '/': 'Divided By ',
                     '**': 'To The Power Of ',
                     '=': 'Equals ',
                     '!=': 'Does Not Equal ',
                     '1': 'One',
                     '2': 'Two',
                     '3': 'Three',
                     '4': 'Four',
                     '5': 'Five',
                     '6': 'Six',
                     '7': 'Seven',
                     '8': 'Eight',
                     '9': 'Nine',
                     '10': 'Ten'}

    for i in string.split():
        string = string.replace(i, changed_value[i])
    return ' '.join(string.split())


def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    result = 0
    for row in range(len(lst)):
        result += lst[row][row] + lst[row][len(lst) - row - 1]
    return result


