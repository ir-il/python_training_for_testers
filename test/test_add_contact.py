# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Iryna", lastname="Ilina", position="QA", company="Lognet",
                      homephone='0639723102', mobilephone="0509723101", workphone='0999723103',
                      secondaryphone='0589723104', address='Friedrich-Engels-Str. 24, 14473 Potsdam, Germany',
                      email2='ololo2@as.sd', email3='qwerty3@df.df',
                      notes="test contact creation")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)