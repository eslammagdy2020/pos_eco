


frappe.ui.form.on('POS Closing Entry', {


    
})


function set_form_data(data, frm) {
    let currency_total = {"USD":0,"EUR":0}
	data.forEach(d => {
		add_to_pos_transaction(d, frm);
		frm.doc.grand_total += flt(d.grand_total);
		frm.doc.net_total += flt(d.net_total);
		frm.doc.total_quantity += flt(d.total_qty);
        if(currency_total[d.currency] != null){
            currency_total[d.currency] += flt(d.grand_total)
        }
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