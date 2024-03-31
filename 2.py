#print('вносим изменеия')
#print('вносим изменеия')

#print('на гитхаб')





# map(func, iterable) - вызывает функцию для кажд iterable
# filter (func, iterable)

# def mult (t):
#     return t*2
# lst = [1,2,3,4,5]
# lst2 = list(map(mult, lst))
# lst2 = list(map(lambda t: t*2, [1,2,3,4,5]))
# print (lst2)

# t = (2.2, 5.9, 9.6)
# t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)

# s = ['a', 'b', 'c']
# sa = [1,2,3,4,5]
# res = list(map(lambda x, y: (x,y), s ,sa))
# print(res)

# s = [1,2,3]
# sa = [4,5,6]
# res = list(map(lambda x, y: (x+y), s, sa))
# print(res)

# t = ('jhgy', 'ggt', 'gtyhj', 'kijuhyt', 'asd')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# Декораторы

# def my_decorator(func): # декор функция
#     def inner():
#         print("-" * 40)
#         func()
#         print("-" * 40)
#     return inner
# @my_decorator # декоратор
# def func_test(): # декор функция
#     print("Hello, I am func 'func_test'")
#
# func_test()





# Строки
# 0b101010 - двоичная сист bin()
# 0o22 - восьмиричная сист oct()
# 0x12 - шестнадцатиричная hex()

# Методы строк
# .find()
# .search()
# .index()
# .endswith() - кончается ли на...
# .startswith() - начинается ли с...
# .isdigit()
# .isalpha() - буквы
# .isalnum() - буквы+цифры
# .islower() - всё нижний регистр(смотрит только на буквы)
# .isupper() - всё верхний регистр(смотрит только на буквы)
# .center(width, char) - отступ относительно width используя char
# .lstrip(char) - убирает char слева (если существуют)
# .rstrip(char) - убирает char справа (если существуют)
# .strip(char) - убирает char с боков (если существуют)
# .replace(old, new, count)
# s.join() - объединяет элементы используя разделитель(s)
# .split(s, max) - разбивает на элементы списка слева используя разделитель(s), max - скок раз исползовать разделитель
# .rsplit() - .split() но начинает справа

# Регулярные выражения
import re
# dir(re) - проверка методов от импорта
# s = 'Я ищу совпадения в 2024. И я их найду в 2 счёта.'
# reg = 'я'
# print(re.findall(reg, s)) #Возвращает список всех совпадений с шаблоном
# print(re.search(reg, s)) #Возвращает первое совпадение с шаблоном
# print(re.match(reg, s)) #Возвращает первое совпадение с шаблоном в начале строки
# print(re.split(reg, s)) #Возвращает список в котром строка разбита по шаблонам
# print(re.sub(reg, "!", s)) #replace




# f = open("test.txt")
# print(*f)
# f.close()