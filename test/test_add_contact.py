# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Iryna", lastname="Ilina", position="QA", company="Lognet", mobile="0509723131", day="13", year="1984", notes="test contact creation"))
    app.session.logout()
