# -*- coding: utf-8 -*-
__author__ = 'Irsen'

from model.group import Group
from random import randrange

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_preconditions"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edited_group_name")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test_preconditions"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(header="edited_header of group"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

#def test_edit_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test_preconditions"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(footer="edited_footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)