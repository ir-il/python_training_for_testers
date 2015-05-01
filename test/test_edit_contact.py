# -*- coding: utf-8 -*-
__author__ = 'Irsen'

from model.contact import Contact

def test_edit_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Iryna-1", lastname="Ilina-1", position="", company="unemployed", mobile="+(380)509723131", day="13", year="1984", notes="this contact was edited"))

