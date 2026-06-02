frappe.ui.form.on("Library Member", {
    refresh: function(frm) {
        frappe.call({
            method: "library_management.ibrary_management.doctype.library_member.library_member.member_details",
            args: {
                membership_type: "Gold",
                active_member: 1
            },
            callback: function(r) {
                console.log(r.message);
                frappe.msgprint( "Gold Active Members Count: " + r.message.length);
            }
        });
    }
});


