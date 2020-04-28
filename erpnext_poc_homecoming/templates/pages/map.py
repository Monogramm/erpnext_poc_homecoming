import frappe
from frappe.www.desk import get_build_version


def get_context(context):
    hooks = frappe.get_hooks()
    context.content = {
        "no_cache": 1,
        "build_version": get_build_version(),
        "include_js": hooks["app_include_js"],
        "include_css": hooks["app_include_css"],
        "sounds": hooks["sounds"],
    }
    return context
