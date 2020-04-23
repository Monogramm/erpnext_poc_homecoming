import frappe


@frappe.whitelist(allow_guest=True)
def get_all_organizations():
    return frappe.get_all("Organization", fields=["location"])
