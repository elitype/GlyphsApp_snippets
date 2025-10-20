Glyphs.clearLog()
Glyphs.showMacroWindow()

font = Glyphs.font
# access nodes and handles

for glyph in font.selection:
	for layer in glyph.layers:
		if layer.name == "Light":
			print(layer.name)
			for path in layer.paths:
				for node in path.nodes:
					print("pt={} x={} y={}" .format(node.index, node.x, node.y))
		if layer.name == "Bold":
			print(layer.name)
			for path in layer.paths:
				for node in path.nodes:
					print("pt={} x={} y={}" .format(node.index, node.x, node.y))
