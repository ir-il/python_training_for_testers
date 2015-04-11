# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Iryna", lastname="Ilina", position="QA", company="Lognet", mobile="0509723131", day="13", year="1984", notes="test contact creation"))
    app.logout()
