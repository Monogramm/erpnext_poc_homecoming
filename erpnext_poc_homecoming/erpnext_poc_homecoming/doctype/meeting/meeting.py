# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import datetime

class Meeting(Document):
	pass

@frappe.whitelist()
def get_events(start, end, filters=None):
	"""Returns events for Gantt / Calendar view rendering.

	:param start: Start date-time.
	:param end: End date-time.
	:param filters: Filters (JSON).
	"""
	from frappe.desk.calendar import get_event_conditions
	conditions = get_event_conditions("Meeting", filters)

	data = frappe.db.sql("""
		select
		`tabMeeting`.title,
		`tabMeeting`.user,
		`tabMeeting`.adviser,
		`tabMeeting`.date_time as 'start'
		from
		`tabMeeting`
		where
		(`tabMeeting`.date_time between %(start)s and %(end)s)
		and `tabMeeting`.docstatus < 2 {conditions}""".format(conditions=conditions),
		{"start": start, "end": end}, as_dict=True, update={"allDay": 0})

	for item in data:
		item.end = item.start + datetime.timedelta(minutes = 60)

	return data
