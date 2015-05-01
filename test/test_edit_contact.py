# -*- coding: utf-8 -*-
__author__ = 'Irsen'

from model.contact import Contact

def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Iryna_Preconditions"))
    app.contact.edit_first_contact(Contact(firstname="Iryna-test editing", notes="this contact was edited"))

def test_edit_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Iryna_Preconditions"))
    app.contact.edit_first_contact(Contact(company="askjdf", notes="this contact was edited 2nd time"))


