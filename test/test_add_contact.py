# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


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
    for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)