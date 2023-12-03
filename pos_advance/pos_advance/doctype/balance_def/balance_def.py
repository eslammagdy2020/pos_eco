# Copyright (c) 2023, beshoyatef31@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe import _ 
from frappe.model.document import Document

class BalanceDef(Document):
	def validate(self) :
		self.validate_condition ()
	def valid_types(self):
		return ['i' ,'u' , 'b' , 'q']
	def validate_condition (self):
		if self.barcode_fromat :
			length_min = 0 
			perfixs = str(self.barcode_fromat).split("-") 
			for i in perfixs :
				if i not in  self.valid_types():
					frappe.throw(f"{i} not accepted ")
				if i == "b" :
					length_min = length_min + int(self.balance_code_length or 0)
				if i == "q" :
					length_min = length_min  + int(self.qty_code_length or 0)	
				if i == "u": 
					length_min = length_min + int(self.uom_code_length)
			if int(self.barcode_min_length) < length_min :
				frappe.throw(_(f"please set Barcode Min Length more than {length_min}"))
				

