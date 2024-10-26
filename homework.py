# Задание
# Напишите программу, которая берет строку "1; 2; 2.5; 3; 5.1; 7; 8.8; 100" и возвращает:
# •список из целых чисел
# •список из чисел с плавающей точкой

def str_to_list_using_separator(s: str, sep=','):
    return list(s.split(sep))


def filter_list(list_):
    int_list = []
    float_list = []
    for el in list_:
        try:
            value = float(el)
            if value.is_integer():
                int_list.append(int(value))
            else:
                float_list.append(value)
        except ValueError:
            continue
    return int_list, float_list


data = "1; 2; 2.5; 3; 5.1; 7; 8.8; 100"
print(filter_list(str_to_list_using_separator(data, '; ')))
print('\n')



# Задание
# Дан кортеж
# student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)
# Выполните пункты ниже. Все выводы должны быть в формате "Средний балл студента: {средний балл}"
# • Выведите фамилию и имя Ивана в формате "Студент: {Фамилия}, {Имя}"
# • Выведите возраст Ивана, если сейчас 2022 год.
# • Напечатайте оценки Ивана через запятую (не список, а числа через запятую).
# • Найдите средний балл Ивана, если оценки хранятся в списке внутри кортежа.
# Сумму элементов списка можно найти с помощью функции sum().
# • Выведите средний балл, округленный до одного знака после запятой.
# Если средняя оценка Ивана больше или равна 8 и он учится на бюджете (последний
# элемент списка, True - бюджет), то он получает повышенную стипендию.
# Выведите True или False.

def get_name(cortege_):
    return cortege_[0].split().__getitem__(0)


def get_surname(cortege_):
    return cortege_[0].split().__getitem__(1)


def print_name_and_surname(cortege_):
    print(f'Студент: {get_surname(cortege_)}, {get_name(cortege_)}')


def calculate_age(cortege_, year) -> int:
    return year - cortege_[1]


def print_age(cortege_):
    print(f'Возраст студента: {calculate_age(cortege_, 2022)}')


def marks(cortege_):
    return cortege_[2]


def print_marks(list_):
    marks_in_string = ', '.join(map(str, list_))
    print(f'Оценки: {marks_in_string}')


def calc_avg_marks(cortege_):
    list_marks = cortege_[2]
    return round(sum(list_marks) / len(list_marks), 1)


def print_avg_mark(cortege_):
    print(f'Средняя оценка: {calc_avg_marks(cortege_)}')


def check_bugdet(cortege_):
    return cortege_[3]


def print_budget(cortege_):
    print(f'Бюджет: {check_bugdet(cortege_)}')


def print_avg_mark__with_condition(cortege_, n):
    if calc_avg_marks(cortege_) >= n and check_bugdet(cortege_):
        print(f'Средняя оценка: {calc_avg_marks(cortege_)} больше {n}')
    else:
        print(f'Средняя оценка: {calc_avg_marks(cortege_)} меньше {n}')


def print_stipendia(cortege_, n):
    if calc_avg_marks(cortege_) >= n and check_bugdet(cortege_):
        print('Стипендия повышенная')
    else:
        print('Стипендия НЕ повышенная')


student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)
mark = 8
print_name_and_surname(student)
print_age(student)
print_marks(marks(student))
print_avg_mark(student)
print_avg_mark__with_condition(student, mark)
print_budget(student)
print_stipendia(student, mark)
print('\n')




# Задание
# Напишите программу, которая бы считала, сколько всего в словаре оценок, которые выше или равны определенному баллу.
# Программа должна принимает на ввод оценку, а выводит количество оценок во всем словаре,
# которые больше этой оценки или равны ей. Пример ввода: 5 Пример вывода: 17
# marks = {
# 'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
# 'John' : [3, 3, 6, 8, 2, 1, 8, 5],
# 'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
# 'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]
# }

def get_list_of_all_marks(dict_):
    list_ = []
    for i in dict_.values():
        for j in i:
            list_.append(j)
    return list_


def count_marks_with_condition(dict_, n):
    count = 0
    for el in get_list_of_all_marks(dict_):
        if el >= n:
            count += 1
    return count


def print_counted_marks(dict_):
    while True:
        s = input('Введите оценку: ')
        try:
            n = int(s)
            break
        except:
            print('Ошибка! Нужно ввести число!')
    print(count_marks_with_condition(dict_, n))


marks = {
    'Mary': [5, 8, 9, 10, 3, 5, 6, 6],
    'John': [3, 3, 6, 8, 2, 1, 8, 5],
    'Alex': [4, 4, 7, 4, 7, 3, 2, 9],
    'Patricia': [2, 1, 6, 8, 2, 3, 7, 4]
}

print_counted_marks(marks)
