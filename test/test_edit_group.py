# -*- coding: utf-8 -*-
__author__ = 'Irsen'

from model.group import Group
from random import randrange


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test_preconditions"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edited_group_name")
    group.id = old_groups[index].id
    app.group.edit_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = map(app.group.clean_group_name, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)