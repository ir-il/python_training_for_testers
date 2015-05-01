# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="Iryna", lastname="Ilina", position="QA", company="Lognet", mobile="0509723131", notes="test contact creation"))
