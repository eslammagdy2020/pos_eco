


frappe.ui.form.on('POS Closing Entry', {

	before_save: async function(frm) {
		// console.log('child-------------')
		frappe.dom.freeze(__('Processing Sales! Please Wait...'));

		frm.set_value("grand_total", 0);
		frm.set_value("net_total", 0);
		frm.set_value("total_quantity", 0);
		frm.set_value("taxes", []);

		for (let row of frm.doc.payment_reconciliation) {
			row.expected_amount = row.opening_amount;
		}

		const pos_inv_promises = frm.doc.pos_transactions.map(
			row => frappe.db.get_doc("POS Invoice", row.pos_invoice)
		);

		const pos_invoices = await Promise.all(pos_inv_promises);
		let currency_array = ["USD","EUR"]
		for (let doc of pos_invoices) {
			if(!currency_array.includes(doc.currency)){
				frm.doc.grand_total += flt(doc.grand_total);
				frm.doc.net_total += flt(doc.net_total);
			}
			frm.doc.total_quantity += flt(doc.total_qty);
			refresh_payments(doc, frm);
			refresh_taxes(doc, frm);
			refresh_fields(frm);
			set_html_data(frm);
		}

		frappe.dom.unfreeze();
	}
    
})


function set_form_data(data, frm) {
    let currency_total = {"USD":0,"EUR":0}
	data.forEach(d => {
		add_to_pos_transaction(d, frm);
        if(currency_total[d.currency] != null){
			currency_total[d.currency] += flt(d.grand_total)
        }else if(currency_total[d.currency] == null){
			frm.doc.grand_total += flt(d.grand_total);
			frm.doc.net_total += flt(d.net_total);			
		}
		frm.doc.total_quantity += flt(d.total_qty);
		refresh_payments(d, frm);
		refresh_taxes(d, frm);
	});
    update_total_fields(frm,currency_total)
}

function update_total_fields(frm,data){
    frm.set_value('grand_usd',data.USD)
    frm.set_value('grand_eur',data.EUR)
    frm.refresh_field("grand_usd");
	frm.refresh_field("grand_eur");
}