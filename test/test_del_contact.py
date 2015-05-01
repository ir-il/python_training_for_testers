# -*- coding: utf-8 -*-
__author__ = 'Irsen'
from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Iryna_Preconditions"))
    app.contact.delete_first_contact()