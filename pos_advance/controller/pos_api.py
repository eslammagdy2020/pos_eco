import frappe


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_supplier_items(doctype, txt, searchfield, start, page_len, filters):
    cond = "and `tabItem Supplier`.supplier = '%s'" % filters.get("supplier") or None
    searchfield = "`tabItem`.name"
    data = frappe.db.sql(
        """select `tabItem`.name,`tabItem`.item_name ,`tabItem`.item_code
            FROM `tabItem`
            inner join `tabItem Supplier`
            on `tabItem Supplier`.parent=`tabItem`.name
			where {key} LIKE %(txt)s {cond}
			order by `tabItem`.name limit %(start)s, %(page_len)s""".format(
            key=searchfield, cond=cond
        ),
        {"txt": "%" + txt + "%", "start": start, "page_len": page_len},
    )
    return data
