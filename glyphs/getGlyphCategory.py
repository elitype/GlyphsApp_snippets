Glyphs.clearLog()
font = Glyphs.font

for glyph in font.selection:
	for layer in glyph.layers:
		if layer.name == 'Light':
			print(glyph.name, glyph.category, glyph.subCategory)
