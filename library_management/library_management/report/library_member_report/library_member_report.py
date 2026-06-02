# Copyright (c) 2026, Saravanan M K and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = ["Member Name:Data:200", "Membership Type:Data:150", "Active Member:Check:120"]
    data = frappe.get_all("Library Member",fields=[ "member_name", "membership_type", "active_member"])
    return columns, data
