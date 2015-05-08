# -*- coding: utf-8 -*-
__author__ = 'Iryna Ilina'

from sys import maxsize


class Contact:


    def __init__(self, firstname=None, lastname=None, position=None, company=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None,
                 address=None, email=None, email2=None, email3=None, all_emails_from_home_page=None, notes=None):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.company = company
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return"%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.homephone, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize