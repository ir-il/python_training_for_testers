# -*- coding: utf-8 -*-
__author__ = 'Irsen'

from model.group import Group

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_preconditions"))
    app.group.edit_first_group(Group(name="edited_group_name"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_preconditions"))
    app.group.edit_first_group(Group(header="edited_header of group"))

def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_preconditions"))
    app.group.edit_first_group(Group(footer="edited_footer"))