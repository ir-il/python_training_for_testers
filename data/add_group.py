__author__ = 'IRSEN'
# -*- coding: utf-8 -*-

from model.group import Group
import random
import string

# при запуске тестов можно выбрать, какой из двух способов (константы или случайные данные) использовать
# для этого нужно заменить в тестах строчку
# from data.add_group import testdata
# на строчку
# from data.add_group import constant as testdata


# задаём эти значения сами
constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

# генерируем случайные значения
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 7), footer=random_string("footer", 5))
    for i in range(5)
#   for name in ["", random_string("name", 10)]
#   for header in ["", random_string("header", 7)]
#   for footer in ["", random_string("footer", 5)]
]