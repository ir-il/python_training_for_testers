# -*- coding: utf-8 -*-
__author__ = 'Irsen'
from model.contact import Contact

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
        self.contact_cache = None

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


    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # start editing of the first contact
        wd.find_elements_by_css_selector("img[alt=\"Редагувати\"]")[index].click()  #поискать более надёжный способ?
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # save changes
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

# Seems that this method is not needed any more (after task 13)
#    def select_first_contact(self):
#        wd = self.app.wd
#        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        # close dialog-box
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            i = 1
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                i = i+1
                lastname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+str(i)+"]/td[2]").text
                firstname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+str(i)+"]/td[3]").text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)