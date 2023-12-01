# Copyright (c) 2023, beshoyatef31@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
import openpyxl
from pos_advance.utils import scan_barcode

class ShelfPrint(Document):
	pass
	def validate_price_list(self):
		selling = frappe.db.get_value('Price List', self.price_list , 'selling')
		if not selling :
			frappe.throw(f"Price list {selling} is not Selling Price List ")
	def validate(self):
		self.validate_price_list()
		self.get_data_from_file()
		self.set_item_price()
	def get_data_from_file(self):
		if not self.sheet_date :
			frappe.throw(_("Please Select excel sheet !"))
		pat = f"{self.sheet_date}".split('/')
		workbook =  openpyxl.load_workbook(frappe.get_site_path('private', 'files', pat[-1]) )
		sheet_obj = workbook.active
		self.items = []
		for i in range(2, int(sheet_obj.max_row) + 1 ) :
			cell_obj = sheet_obj.cell(row = i, column = 1)
			item = scan_barcode(cell_obj.value)
			if not item :
				frappe.msgprint(_(f"Can not find Barcode {cell_obj.value} "))
			if item :
				row = self.append("items" , {})
				row.item =item.get("item_code")
				row.item_name  =  frappe.db.get_value("Item" , 
				{"item_code" : row.item  } ,"item_name" )	
				row.uom = item.get("uom")
				row.code = cell_obj.value
			# print(workbook)
	def set_item_price(self):
		if self.items and len(self.items) > 0 :
			for item in self.items :
				item.price = frappe.db.get_value("Item Price" ,
				  {"price_list" :self.price_list , "uom" :item.uom , "item_code" : item.item}
				  ,"price_list_rate" )
				item.price_after_discount = item.price
				item.barcode = item.code 