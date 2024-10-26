# Задание
# Напишите программу, которая проверяет, являются ли все элементы списка палиндромами
# (строки, которые читаются слева направо и справа налево одинаково).
# Можно использовать циклы, list comprehantion, all
# Пример. Используйте этот список: ['aba', 12321, 'aaccdccaa'] Вывод: True

# import random
# data = [random.randint(-1, 100) for _ in range(20)]
# map_data = map(lambda x: x >= 0, data)
# print(any(map_data))

# data = ['aba', 12321, 'aaccdccaa']
# def all_is_palindrome(list_):
#     return all(map(lambda el: el == el[::-1], map(str, list_)))
#
# print(all_is_palindrome(data))


# Задание
# Напишите функцию my_log(), которая принимает на вход список чисел, и возвращает список их натуральных логарифмов.
# Если число меньше или равно 0, на его месте в возвращаемом списке должно быть None.
# Пример: Входные данные: [1, 3, 2.5, -1, 9, 0, 2.71]
# Выходные данные: [0.0, 1.0986122886681098, 0.9162907318741551, None, 2.1972245773362196, None,
# 0.9969486348916096]

# from math import log
# def my_log(list_):
#     # return list(map(lambda x: log(x) if x > 0 else None, list_))
#     return [log(el) if el > 0 else None for el in list_]
#
# data = [1, 3, 2.5, -1, 9, 0, 2.71]
# print(my_log(data))


# Задание
# Напишите программу, которая принимает на вход список слов такого вида:
# words = ["Speak ","to", "me ", "of", "Florence" ,"And ", "of", "the",
# "Renaissance"]
# а возвращает список
# words_clean = ["speak", "to", "me", "of", "florence", "and", "of", "the",
# "renaissance"]
# Другими словами, программа убирает пробелы в словах и приводит все слова к
# нижнему регистру.

# def clean_list(data):
#     return [s.lower().strip() for s in data]
#     # return list(map(str.lower, map(str.strip, data)))
#
# words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]
# print(clean_list(words))

# def clean_list(data):
#     res = []
#     for el in data:
#         res.append(el.lower())
#     return res
#
# words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]
# print(clean_list(words))


# Задание
# Дан список студентов.
# students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
# Оценки студентов за контрольную работу сохранены в словаре grades:
# grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня":
# 10}
# 1. Напишите программу, которая выводит на экран имя студента из списка students и его
# оценку.
# Если оценки студента из списка students нет, то на экран должно выводиться имя
# студента и сообщение "Контрольную работу не писал(а)".
# 2. Напишите программу, которая выводит на экран имена студентов, которые получили
# отличные оценки (8 и выше).
# 3. Напишите программу, которая сохраняет имена студентов, получивших хорошие и
# отличные оценки, в список good, а получивших удовлетворительные и плохие оценки –
# в список bad.
# students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
# grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня":
# 10} # get_student_grade(students, grades) # good_grade(grades, 9) good_bad(grades)
# {'good': ['Петя', 'Марина', 'Ваня'], 'bad': ['Вася', 'Люба', 'Коля']}

# def get_student_grade(data_list, data_dict):
#     for student in data_list:
#         if student in data_dict:
#             print(f'{student} имеет оценку {data_dict.get(student)}')
#         else:
#             print(f'{student} контрольную работу не писал(а)')
#
# students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
# grades = {"Вася": 4, "Петя": 9, "Марина": 8, "Люба": 4, "Коля": 5, "Ваня": 10}
# get_student_grade(students, grades)
#
# def print_good_grade(data_dict, n=8):
#     res = []
#     for k,v in data_dict.items():
#         if v >= n:
#             res.append(k)
#     return res
#
# # print_good_grade(grades, 8)
# print(print_good_grade(grades, 8))
#
# def good_bad(data_dict, n):
#     good, bad = [], []
#     for k,v in data_dict.items():
#         if v >= n:
#             good.append(k)
#         else:
#             bad.append(k)
#     return good, bad
#
# def good_bad_2(data_dict, n):
#     good = print_good_grade(data_dict, n)
#     return good, list(filter(lambda x: x not in good, data_dict.keys()))
#
# print(good_bad(grades, 8))
# print(good_bad_2(grades, 8))


# Задание
# Вам дан словарь с именами студентов и их оценками за курс по десятибаллной шкале.
# Напишите программу, которая бы считала среднюю оценку за курс и округляла ее (используйте функцию round()).
# Чтобы найти среднюю оценку нужно сложить оценки всех студентов за курс и разделить сумму на количество студентов.
# Найти сумму элементов списка, можно функцией sum().
# Так, первый курс - это нулевой элемент списка оценок каждого студента.
# Программа должна приниматься на ввод номер курса (от 1 до 8, обратите внимание, что не от 0 до 7),
# а выводить среднюю оценку за этот курс.
# marks = {
# 'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
# 'John' : [3, 3, 6, 8, 2, 1, 8, 5],
# 'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
# 'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]
# }
# Пример ввода: 1 Пример вывода: Курс 1 - 4

# def avg_grade_for_course(data_dict, number):
#     data = []
#     for student_grades in data_dict.values():
#         data.append(student_grades[number - 1])
#     return round(sum(data) / len(data))
#
# def avg_grade_for_course_2(data_dict, number):
#     data = list(zip(*data_dict.values()))
#     return round(sum(data[number - 1]) / len(data[number - 1]))
#
# def main():
#     while True:
#         s = input('Введи номер курса: ')
#         try:
#             n = int(s)
#             break
#         except:
#             print('Ошибка! Нужно ввести число!')
#     print(f'Средняя оценка за курс {n}: {avg_grade_for_course(marks, n)}')
#
# marks = {
#     'Mary': [5, 8, 9, 10, 3, 5, 6, 6],
#     'John': [3, 3, 6, 8, 2, 1, 8, 5],
#     'Alex': [4, 4, 7, 4, 7, 3, 2, 9],
#     'Patricia': [2, 1, 6, 8, 2, 3, 7, 4]
# }
#
# main()




# Задание
# После заказа в Интернет-магазине корзина покупателя примет следующий вид:
# user = {
# 'Камин комплект Старый Замок': {'count': 1, 'price': 28490},
# 'Полусапоги Betsy':{'count': 2, 'price': 2399},
# 'Семь навыков высокоэффективных людей':{'count': 1, 'price': 437}
# }
# Определите общую стоимость заказа.

def mul_el(list_):
    return list_[0] * list_[1]

def sum_(data_dict):
    data = []
    for el in data_dict.values():
        data.append(mul_el(list(el.values())))
    return sum(data)

def sum_2(data_dict):
    data = []
    for el in data_dict.values():
        data.append(el['count'] * el['price'])
    return sum(data)

user = {
'Камин комплект Старый Замок': {'count': 1, 'price': 28490},
'Полусапоги Betsy':{'count': 2, 'price': 2399},
'Семь навыков высокоэффективных людей':{'count': 1, 'price': 437}
}

print(sum_(user))
print(sum_2(user))

