# -*- coding: utf-8 -*-
__author__ = 'Irsen'

class ContactHelper():

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("Додати контакт").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.position)
        self.change_field_value("company", contact.company)
        self.change_field_value("mobile", contact.mobile)
        #self.change_field_value("bday", contact.day)  # разобраться, как передавать эти параметры (день, год и месяц)
        #self.change_field_value("byear", contact.year)
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            #wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()  #figure out how to make the month parameter (values "February", "3" or "Лютий" ignored)
        self.change_field_value("notes", contact.notes)


    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # start editing of the first contact
        wd.find_element_by_css_selector("img[alt=\"Редагувати\"]").click()  #поискать более надёжный способ?
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # save changes
        wd.find_element_by_name("update").click()
        self.app.open_home_page()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        # close dialog-box
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))