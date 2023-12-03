from . import __version__ as app_version

app_name = "pos_advance"
app_title = "Pos Advance"
app_publisher = "beshoyatef31@gmail.com"
app_description = "POS APP"
app_email = "beshoyatef31@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pos_advance/css/pos_advance.css"
# app_include_js = "/assets/pos_advance/js/pos_advance.js"

# include js, css files in header of web template
# web_include_css = "/assets/pos_advance/css/pos_advance.css"
# web_include_js = "/assets/pos_advance/js/pos_advance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pos_advance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page /home/beshoy/frappe-bench/apps/pos_advance/pos_advance/pages/point_of_sale/point_of_sale.js
page_js = {"point-of-sale": "public/js/point_of_sales.js"}

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "pos_advance.utils.jinja_methods",
# 	"filters": "pos_advance.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "pos_advance.install.before_install"
# after_install = "pos_advance.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "pos_advance.uninstall.before_uninstall"
# after_uninstall = "pos_advance.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "pos_advance.utils.before_app_install"
# after_app_install = "pos_advance.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "pos_advance.utils.before_app_uninstall"
# after_app_uninstall = "pos_advance.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pos_advance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways
override_whitelisted_methods = {
    "erpnext.selling.page.point_of_sale.point_of_sale.get_items": "pos_advance.utils.get_items" ,
    "erpnext.stock.utils.scan_barcode": "pos_advance.utils.scan_barcode"
}
# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# } /erpnext.stock.get_item_details.get_item_details
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pos_advance.tasks.all"
# 	],
# 	"daily": [
# 		"pos_advance.tasks.daily"
# 	],
# 	"hourly": [
# 		"pos_advance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pos_advance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"pos_advance.tasks.monthly"
# 	],
# }

# Testing
# -------

doctype_js = {
    "POS Closing Entry": "public/js/pos_closing_entry.js",
    "Purchase Order": "public/js/purchase_order.js",
    "Purchase Invoice": "public/js/purchase_invoice.js",
    "Purchase Receipt": "public/js/purchase_receipt.js",
    "Supplier Quotation": "public/js/supplier_quotation.js",
}
# before_tests = "pos_advance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"erpnext.stock.utils.scan_barcode": "pos_advance.utils.scan_barcode"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pos_advance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["pos_advance.utils.before_request"]
# after_request = ["pos_advance.utils.after_request"]

# Job Events
# ----------
# before_job = ["pos_advance.utils.before_job"]
# after_job = ["pos_advance.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"pos_advance.auth.validate"
# ]


domains = {
    "POS": "pos_advance.domains.pos",
}
