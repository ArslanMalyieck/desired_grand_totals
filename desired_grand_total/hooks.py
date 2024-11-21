app_name = "desired_grand_total"
app_title = "Desired Grand Total"
app_publisher = "Arslan"
app_description = "An ERPNext app to adjust Sales Invoice grand total based on user-defined value and automatically update item rates."
app_email = "malikarslan000009@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "desired_grand_total",
# 		"logo": "/assets/desired_grand_total/logo.png",
# 		"title": "Desired Grand Total",
# 		"route": "/desired_grand_total",
# 		"has_permission": "desired_grand_total.api.permission.has_app_permission"
# 	}
# ]
# doc_events = {
#     "Sales Invoice": {
#         "validate": "desired_grand_total.customizations.sales_invoice.calculate_reduction_percent"
#     }
# }

# Fixtures
# Ensure that the custom fields are created when the app is installed
fixtures = [
    {
        "dt": "Custom Field",  # Specifying the "Custom Field" doctype
        "filters": [
            ["name", "in", ["section_break_101","desired_grand_total","column_break_101", "reduction_percent"]]  # Filter custom fields related to desired_grand_total
        ]
    }
]
# Includes in <head>
# ------------------
doctype_js = {"Sales Invoice": "public/js/sales_invoice.js"}
# include js, css files in header of desk.html
# app_include_css = "/assets/desired_grand_total/css/desired_grand_total.css"
# app_include_js = "/assets/desired_grand_total/js/desired_grand_total.js"
# app_include_js = "/assets/desired_grand_total/js/sales_invoice.js"
# include js, css files in header of web template
# web_include_css = "/assets/desired_grand_total/css/desired_grand_total.css"
# web_include_js = "/assets/desired_grand_total/js/desired_grand_total.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "desired_grand_total/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "desired_grand_total/public/icons.svg"

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
# 	"methods": "desired_grand_total.utils.jinja_methods",
# 	"filters": "desired_grand_total.utils.jinja_filters"
# }

# Installation
# ------------
after_install = "desired_grand_total.customizations.sales_invoice.create_sales_invoice_custom_fields"

# before_install = "desired_grand_total.install.before_install"
# after_install = "desired_grand_total.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "desired_grand_total.uninstall.before_uninstall"
# after_uninstall = "desired_grand_total.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "desired_grand_total.utils.before_app_install"
# after_app_install = "desired_grand_total.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "desired_grand_total.utils.before_app_uninstall"
# after_app_uninstall = "desired_grand_total.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "desired_grand_total.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
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
# 		"desired_grand_total.tasks.all"
# 	],
# 	"daily": [
# 		"desired_grand_total.tasks.daily"
# 	],
# 	"hourly": [
# 		"desired_grand_total.tasks.hourly"
# 	],
# 	"weekly": [
# 		"desired_grand_total.tasks.weekly"
# 	],
# 	"monthly": [
# 		"desired_grand_total.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "desired_grand_total.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "desired_grand_total.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "desired_grand_total.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["desired_grand_total.utils.before_request"]
# after_request = ["desired_grand_total.utils.after_request"]

# Job Events
# ----------
# before_job = ["desired_grand_total.utils.before_job"]
# after_job = ["desired_grand_total.utils.after_job"]

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
# 	"desired_grand_total.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

