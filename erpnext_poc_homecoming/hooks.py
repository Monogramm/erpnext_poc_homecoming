# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for hooks."""

from __future__ import unicode_literals


app_name = "erpnext_poc_homecoming"
app_title = "ERPNext POC Homecoming"
app_publisher = "Monogramm"
app_description = "POC of an ERPNext application to manage individual homecoming travel projects."
app_icon = "octicon octicon-home"
app_color = "forestgreen"
app_email = "opensource@monogramm.io"
app_license = "AGPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_poc_homecoming/css/erpnext_poc_homecoming.css"
# app_include_js = "/assets/erpnext_poc_homecoming/js/erpnext_poc_homecoming.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_poc_homecoming/css/erpnext_poc_homecoming.css"
# web_include_js = "/assets/erpnext_poc_homecoming/js/erpnext_poc_homecoming.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#    "Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_poc_homecoming.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_poc_homecoming.install.before_install"
# after_install = "erpnext_poc_homecoming.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_poc_homecoming.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#     "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#     "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#     "*": {
#         "on_update": "method",
#         "on_cancel": "method",
#         "on_trash": "method"
#    }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#     "all": [
#         "erpnext_poc_homecoming.tasks.all"
#     ],
#     "daily": [
#         "erpnext_poc_homecoming.tasks.daily"
#     ],
#     "hourly": [
#         "erpnext_poc_homecoming.tasks.hourly"
#     ],
#     "weekly": [
#         "erpnext_poc_homecoming.tasks.weekly"
#     ]
#     "monthly": [
#         "erpnext_poc_homecoming.tasks.monthly"
#     ]
# }

# Testing
# -------

# before_tests = "erpnext_poc_homecoming.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": "erpnext_poc_homecoming.event.get_events"
# }

