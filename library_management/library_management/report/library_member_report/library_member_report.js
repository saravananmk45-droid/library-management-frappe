// Copyright (c) 2026, Saravanan M K and contributors
// For license information, please see license.txt

frappe.query_reports["Library Member Report"] = {
    filters: [
        {
            fieldname: "membership_type", label: "Membership Type", fieldtype: "Select", options: "\nGold\nSilver\nPlatinum"
        },
        {
            fieldname: "active_member", label: "Active Member", fieldtype: "Check"
        }
    ]
};
