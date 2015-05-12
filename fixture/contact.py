# -*- coding: utf-8 -*-
__author__ = 'Irsen'
from model.contact import Contact
import re


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
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.position)
        self.change_field_value("company", contact.company)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("notes", contact.notes)
        # self.change_field_value("bday", contact.day)  # разобраться, как передавать эти параметры (день, год и месяц)
        # self.change_field_value("byear", contact.year)
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()
        # figure out how to make the month parameter (values "February", "3" or "Лютий" ignored)

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # save changes
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        # close dialog-box
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

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
            for row in wd.find_elements_by_name("entry"):
                id = row.find_element_by_name("selected[]").get_attribute("value")
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
#               lastname = row.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+str(i)+"]/td[2]").text
#               firstname = row.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+str(i)+"]/td[3]").text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                       address=address, email=email, email2=email2, email3=email3)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_emails_like_on_home_page(self, contact):
        return '\n'.join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

    def contact_like_on_home_page(self, contact):
        contact = contact
        firstname = contact.firstname.strip()
        lastname = contact.lastname.strip()
        all_phones = self.merge_phones_like_on_home_page(contact)
        all_emails = self.merge_emails_like_on_home_page(contact)
        return Contact(lastname=lastname, firstname=firstname, id=contact.id,
                                                  all_phones_from_home_page=all_phones, address=contact.address,
                                                  all_emails_from_home_page=all_emails)