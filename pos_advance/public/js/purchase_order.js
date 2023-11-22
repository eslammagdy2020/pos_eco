


frappe.ui.form.on('Purchase Order', {
	
	onload:function(frm){
		frm.events.setup_custom_query(frm)
	},

	refresh:function(frm){
		frm.events.setup_custom_query(frm)
	},

	setup_custom_query:function(frm){
		frm.set_query('item_code', 'items', function() {
			return {
				query: 'pos_advance.controller.pos_api.get_supplier_items',
				filters: {
					supplier: frm.doc.supplier || ''
				}
			}
		})
	}
    
})

frappe.ui.form.on('Purchase Order Item',{
	item_code: function (frm, cdt, cdn) {
		// var row = frappe.get_doc(cdt, cdn);
		if(!frm.doc.supplier){
			frm.clear_table('items')
			frm.refresh_field('items')
			frappe.throw(__("Please Select Supplier First"))
		}
	}
})

