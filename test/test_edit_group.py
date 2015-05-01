# -*- coding: utf-8 -*-
__author__ = 'Irsen'

from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="edited_group", header="edited_IIr_header", footer="edited_IIr_footer"))