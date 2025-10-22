Glyphs.clearLog()
font = Glyphs.font
# Decompose components in layers starting wiht 'Color'
for glyph in font.selection:
	for layer in glyph.layers:
		if layer.name.startswith('Color'):
			if layer.components:
				for component in layer.components:
					component.decompose()
			else:
				print(glyph.name, 'has no components')
