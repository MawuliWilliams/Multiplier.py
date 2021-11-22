"""
Program: multiplier.py
Author: Mawuli 11/17/21

*** Note: the file breezypythongui.py MUST be in the same
directory as this file for the application to work.***
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class Multiplier(EasyFrame):

	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Multiplier", width = 320, height = 180)
		titleFont = Font(family = "Arial", size = 20)
		self.titleLabel = self.addLabel(text = "Multiplier X2",
			row = 0, column = 0, columnspan = 2, sticky = "NSEW", font = titleFont)
		self.addLabel(text = "Enter a number", row = 1, column = 0)
		self.inputField = self.addIntegerField(value = 0, row = 1, column = 1)
		self.addButton(text = "Calculate!", row = 2, column = 0, columnspan = 2, command = self.compute)
		self.addLabel(text = "The result:", row = 3, column = 0)
		self.outputField = self.addIntegerField(value = 0, row = 3, column = 1, state = "readonly")

    #Event handeling method
	def compute(self):
		#Take the user input and multiply by 2 and display the result

		num = self.inputField.getNumber()
		result = num * 2
		self.outputField.setNumber(result)


# definition of the main() method for program entry
def main():
	"""Instantiates an object from the class in the graphics loop"""
	Multiplier().mainloop() 

# global call to the main() method
main()