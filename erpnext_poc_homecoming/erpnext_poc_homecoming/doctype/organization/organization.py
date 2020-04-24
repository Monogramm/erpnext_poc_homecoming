# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator


class Organization(WebsiteGenerator):
    pass
    # def get_context(self, context): # it doesnt work right now
    #     context['gqq'] = "qqqq"
    #     context.update({
    #         "mail": "fdsa",
    #         "address_info": frappe.get_doc("Address", self.addressaa)
    #     })
    #     return context


@frappe.whitelist(allow_guest=True)
def get_address(address_title):
    return frappe.get_doc("Address", address_title)


def get_list_context(context=None):
    context.update({
        "show_sidebar": True,
        "show_search": True,
        'no_breadcrumbs': True,
        "doctype": "Organization",
        "title": _("Organization"),
        "row_template": "erpnext_poc_homecoming/doctype/organization/templates/organization_row.html",
    })


@frappe.whitelist(allow_guest=True)
def get_list_map():
    return frappe.get_all("Organization", fields=["title", "route", "location"])
