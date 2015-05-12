# -*- coding: utf-8 -*-
__author__ = 'Irsen'

from model.contact import Contact
from random import randrange


def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Iryna_Preconditions"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Iryna-test editing"+str(index), notes="this contact was edited")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname #костыльчик =(
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(app.contact.contact_like_on_home_page, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


