# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Iryna", lastname="Ilina", position="QA", company="Lognet", mobile="0509723131", day="13", year="1984", notes="test contact creation"))
    app.session.logout()
