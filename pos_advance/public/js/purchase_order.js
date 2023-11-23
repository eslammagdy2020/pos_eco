


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
	},
	validate_item_uom:function(frm,cdt,cdn){
		let row=locals[cdt][cdn]
		frappe.call({
			method:"pos_advance.controller.purchase_order_api.validate_item_uom",
			args:{
				item_name:row.item_code,
				uom:row.uom,
			},
			callback:function(r){
				let res = r.message
				if(res.flage==false){
					frappe.model.set_value(row.doctype, row.name, 'uom', '');
					frm.refresh_field('items')
					frappe.throw(__(`UOM Value Should Be In (${res.avail_uom})`))
				}
			}
		})
	}
    
})

frappe.ui.form.on('Purchase Order Item',{
	item_code: function (frm, cdt, cdn) {
		if(!frm.doc.supplier){
			frm.clear_table('items')
			frm.refresh_field('items')
			frappe.throw(__("Please Select Supplier First"))
		}
	},
	uom: function (frm, cdt, cdn) {
		var row = locals[cdt][cdn]
		if(row.uom){
			frm.events.validate_item_uom(frm,cdt,cdn)
		}
	}
})

