frappe.provide('erpnext.PointOfSale');

frappe.pages['point-of-sale'].on_page_load = function(wrapper) {
	frappe.ui.make_app_page({
		parent: wrapper,
		title: __('Eco POS'),
		single_column: true
	});

	frappe.require('point-of-sale-advance.bundle.js', function() {
		wrapper.pos = new erpnext.PointOfSale.Controller(wrapper);
		window.cur_pos = wrapper.pos;
	});
};

frappe.pages['point-of-sale'].refresh = function(wrapper) {
	if (document.scannerDetectionData) {
		onScan.detachFrom(document);
		wrapper.pos.wrapper.html("");
		wrapper.pos.check_opening_entry();
	}
};


// frappe.provide('erpnext.PointOfSale');

// frappe.pages['point-of-sale'].on_page_load = function(wrapper) {

// 	frappe.require('pos_advance.js', function() {
// 		wrapper.pos = new erpnext.PointOfSale.Controller(wrapper);
// 		window.cur_pos = wrapper.pos;
// 	});
// }