


frappe.ui.form.on('Purchase Receipt', {
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

frappe.ui.form.on('Purchase Receipt Item',{
	uom: function (frm, cdt, cdn) {
		var row = locals[cdt][cdn]
		if(row.uom){
			frm.events.validate_item_uom(frm,cdt,cdn)
		}
	}
})

