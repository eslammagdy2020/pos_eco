from __future__ import unicode_literals


data = {
    "custom_fields": {
        "POS Closing Entry": [
            {
                "fieldname": "column_break_",
                "insert_after": "total_quantity",
                "fieldtype": "Column Break",
            },
            {
                "label": "Grand Total(USD)",
                "fieldname": "grand_usd",
                "fieldtype": "Float",
                "insert_after": "column_break_",
                "default": 0,
            },
            {
                "label": "Grand Total(EUR)",
                "fieldname": "grand_eur",
                "fieldtype": "Float",
                "insert_after": "grand_usd",
                "default": 0,
            },
        ],
    }
}
