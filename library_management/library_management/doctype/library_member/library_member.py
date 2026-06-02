# Copyright (c) 2026, Saravanan M K and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    def validate(self):
        if not self.member_name:
            frappe.throw("Member Name is mandatory")
        allowed_types = ["Gold", "Silver", "Platinum"]
        if self.membership_type not in allowed_types:
            frappe.throw("Invalid Membership Type")
    def before_save(self):
        if self.member_name:
            self.custom_membership_id = "LIB-" + self.member_name.upper()
    def after_insert(self):
        frappe.msgprint(f"Welcome {self.member_name} to Library")
    def get_active_members(self):
        active_members = frappe.get_all("Library Member", filters={"active_member": 1}, fields=["member_name", "membership_type"])
        frappe.msgprint(str(active_members))
def member_created(doc, method):
    frappe.msgprint(f"New Member Created: {doc.member_name}")
@frappe.whitelist()
def get_gold_members():
    return frappe.get_all("Library Member", filters={"membership_type": "Gold"}, fields=["name", "member_name", "membership_type"])
@frappe.whitelist()
def hello_library(name=None):
    if not name:
        name = "Guest"
    return "Welcome to Library API"
@frappe.whitelist()
def member_details(membership_type=None, active_member=None):
    filters = {}
    if membership_type:
        filters["membership_type"] = membership_type
    if active_member:
        filters["active_member"] = active_member
    members = frappe.get_all( "Library Member", filters=filters, feilds=["member_name", "membership_type", "active_member"])
    return members

