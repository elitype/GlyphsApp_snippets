Glyphs.clearLog()
Glyphs.showMacroWindow()

font = Glyphs.font

for glyph in font.selection:
	for layer in glyph.layers:
		if layer.anchors:
			layer.anchors = None
			print('Removed anchors from {} {}' .format(layer.parent.name, layer.name))
		else:
			print(glyph.name, 'no anchors')
