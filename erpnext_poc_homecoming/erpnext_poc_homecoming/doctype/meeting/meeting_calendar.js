// Copyright (c) 2020, Monogramm and contributors
// For license information, please see license.txt

frappe.views.calendar['Meeting'] = {
    field_map: {
		"start": "start",
		"end": "end",
		"id": "title",
		"title": "user",
		"allDay": "allDay"
    },
	order_by: "date_time",
    gantt: true,
    get_events_method: 'erpnext_poc_homecoming.erpnext_poc_homecoming.doctype.meeting.meeting.get_events'
};
