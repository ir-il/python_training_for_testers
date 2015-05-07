# -*- coding: utf-8 -*-
__author__ = 'Irsen'

from model.contact import Contact

def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Iryna_Preconditions"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Iryna-test editing", notes="this contact was edited")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname #костыльчик =(
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_contact_company(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Iryna_Preconditions"))
#    app.contact.edit_first_contact(Contact(company="askjdf", notes="this contact was edited 2nd time"))


