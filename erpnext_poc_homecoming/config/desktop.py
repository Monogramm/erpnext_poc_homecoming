# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for desktop."""

from __future__ import unicode_literals

from frappe import _


def get_data():
    return [
        {
            "module_name": "ERPNext POC Homecoming",
            "color": "forestgreen",
            "icon": "octicon octicon-home",
            "type": "module",
            "label": _("ERPNext POC Homecoming")
        }
    ]
