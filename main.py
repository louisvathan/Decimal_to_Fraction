import kivy
from kivy import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '450')
Config.set('graphics', 'minimum_width', '400')
Config.set('graphics', 'minimum_height', '300')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import pyperclip

kivy.require("2.0.0")

from frac_conv_func import decimal_to_fraction


class MyRoot(BoxLayout):
	
	def __init__(self):
		super(MyRoot, self).__init__()
		# INITIAL CONDITIONS
		self.decimal = 0
		self.denominator = 64
		self.rounding = "Round to Nearest Fraction"
		self.middle_condition = "to Next"

	def denominator_select(self, text):
		self.denominator = int(text)
		self.rounding = self.rounding_input.text
		self.middle_condition = self.middle_condition_input.text
		self.operation()
	
	def rounding_select(self, text):
		self.denominator = self.denominator_input.text
		self.rounding = text
		self.middle_condition = self.middle_condition_input.text
		self.operation()
	
	def middle_condition_select(self, text):
		self.denominator = self.denominator_input.text
		self.rounding = self.rounding_input.text
		self.middle_condition = text
		self.operation()
		
	def operation(self):
		if self.decimal_input.text == "":
			self.output_label.text = "-"
		else:
			decimal = self.decimal_input.text
			self.output_label.text = decimal_to_fraction(float(decimal), int(self.denominator), self.rounding, self.middle_condition)

	def copy(self):
		if self.output_label.text == "-" and self.decimal_input.text == "":
			pyperclip.copy("")
		else:
			self.operation()
			pyperclip.copy(self.output_label.text)

	
class ConvertFraction(App):
	
	def build(self):
		return MyRoot()

convertFraction= ConvertFraction()
convertFraction.run()