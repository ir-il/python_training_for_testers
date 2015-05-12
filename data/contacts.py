__author__ = 'IRSEN'
# -*- coding: utf-8 -*-

from model.contact import Contact

testdata = [
    Contact(firstname="firstname1", lastname="lastname1",
            position="position1", company="company1",
            homephone="H:123456789", mobilephone="M:123123123", workphone="W:00012123",
            secondaryphone="S:456126546", address="address sdfkh shdkjfh 456sdf 4560",
            email="email1@ddf.sfd",
            notes="adfdsafadsf"),
    Contact(firstname="firstname2", lastname="lastname2",
            position="position2", company="company2",
            homephone="123456789", mobilephone="123123123", workphone="00012123",
            secondaryphone="456126546", address="address Shevchenko 45/60",
            email="email222@ddf.sfd",
            notes="fdd 2e d32")
]
