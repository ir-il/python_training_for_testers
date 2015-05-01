__author__ = 'Irsen'

def test_add_contact(app):
    app.contact.delete_first_contact()