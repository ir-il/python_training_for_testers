# -*- coding: utf-8 -*-
__author__ = 'Irsen'

from model.contact import Contact
from random import randrange

def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Iryna_Preconditions"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Iryna-test editing"+str(index), notes="this contact was edited")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname #костыльчик =(
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_contact_company(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Iryna_Preconditions"))
#    app.contact.edit_first_contact(Contact(company="askjdf", notes="this contact was edited 2nd time"))


