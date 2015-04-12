# -*- coding: utf-8 -*-
from model.group import Group

def test_test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="New_group", header="IIr_header", footer="IIr_footer"))
    app.session.logout()


def test_test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
