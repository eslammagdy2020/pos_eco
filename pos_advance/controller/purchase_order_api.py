import frappe
from frappe import _


@frappe.whitelist()
def validate_item_uom(item_name, uom):
    sql = f"""
    SELECT `tabUOM Conversion Detail`.uom  fROM `tabUOM Conversion Detail`
    INNER JOIN `tabItem`
        ON `tabUOM Conversion Detail`.parent =`tabItem`.name
        where `tabItem`.name='{item_name}'
    """
    avail_uom = frappe.db.sql_list(sql)
    flage = True if uom in avail_uom else False
    return {"flage": flage, "avail_uom": avail_uom}
