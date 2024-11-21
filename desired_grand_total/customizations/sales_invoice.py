import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def create_sales_invoice_custom_fields():
    custom_fields = {
        "Sales Invoice": [
            {
                "fieldname": "section_break_101",
                "fieldtype": "Section Break",
                "label": "Adjustment Fields",
                "insert_after": "total_taxes_and_charges",
                "reqd": 0,
            },
            {
                "fieldname": "desired_grand_total",
                "label": "Desired Grand Total",
                "fieldtype": "Currency",
                "insert_after": "section_break_101",  # Inserted after the section break
                "reqd": 0,
                "description": "Enter the desired grand total.",
                "precision": 2
            },
            {
                "fieldname": "column_break_101",
                "fieldtype": "Column Break",
                "insert_after": "desired_grand_total",  # Inserted after the desired grand total field
            },
            {
                "fieldname": "reduction_percent",
                "label": "Reduction Percent",
                "fieldtype": "Percent",
                "insert_after": "column_break_101",  # Inserted after the column break
                "reqd": 0,
                "description": "Reduction percentage based on desired grand total."
            },
        ]
    }
    create_custom_fields(custom_fields, ignore_validate=True)
