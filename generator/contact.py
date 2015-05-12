__author__ = 'IRSEN'
# -*- coding: utf-8 -*-

from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
#   symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    numbers = string.digits + " "*5
#   numbers = string.digits + string.punctuation + " "*5
    return prefix + "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=random_string("firstname", 7), lastname=random_string("lastname", 7),
            position=random_string("position", 5), company=random_string("company", 10),
            homephone=random_number("H", 9), mobilephone=random_number("M", 9), workphone=random_number("W", 9),
            secondaryphone=random_number("S", 9), address=random_string("address", 15),
            email=random_string("email", 7), email2=random_string("email2", 8),
            notes=random_string("notes", 15))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))