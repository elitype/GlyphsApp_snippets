# -*- coding: utf-8 -*-
#MenuTitle: Check tabular width of selected glyphs

from vanilla import Window, TextBox, EditText, Button

class TabularToolWindow:
	def __init__(self):
		self.font = Glyphs.font # fuente
		self.selectedLayers = self.font.selectedLayers # Selected glyphs, in Glyphs app they are called layers
		toppad = 10
		leftpad = 20
		leading = 30
		w = 200
		h = 80
		buttonWidth = 50
		buttonHeight = 50
		self.w = Window((100, 100, w, h), 'Tabular Tool')
		 # Text box, left padding, top padding, width, height from left to right and top to bottom
		self.w.textBox = TextBox((leftpad, toppad, 100, 20), "Tabular width:")
		self.w.tabWidth = EditText((120, 10, 50, 20), sizeStyle='small')
		 
		self.w.button = Button((110, 40, 60, 20), "Check", callback=self.buttonCallback)
		self.w.setDefaultButton( self.w.button )
		# open the window
		self.w.open()
		self.w.makeKey()

	def showMacro(self, outputText):
		Glyphs.clearLog()
		print(outputText)
		Glyphs.showMacroWindow()

	def	buttonCallback(self, sender):
		tabWidth = int(self.w.tabWidth.get())
		self.showMacro('Checked glyphs in {}' .format(self.font.selectedFontMaster.name))
		for thisLayer in self.selectedLayers:
			if tabWidth != thisLayer.width:
				print('⚠️ {} {}' .format(thisLayer.width, thisLayer.parent.name))
			else:
				print('✅ {}'.format(thisLayer.parent.name))

TabularToolWindow()
