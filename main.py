import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require("2.1.0")

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
	
	def rounding_select(self, text):
		self.rounding = text
	
	def middle_condition_select(self, text):
		self.middle_condition = text
		
	def button_trigger(self):
		if self.decimal_input.text == "":
			pass
		else:
			decimal = self.decimal_input.text
			self.output_label.text = decimal_to_fraction(float(decimal), self.denominator, self.rounding, self.middle_condition)

	
class ConvertFraction(App):
	
	def build(self):
		return MyRoot()

convertFraction= ConvertFraction()
convertFraction.run()