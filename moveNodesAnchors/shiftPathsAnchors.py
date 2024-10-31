Glyphs.clearLog()
Glyphs.showMacroWindow()

font = Glyphs.font
# shifts nodes and anchors, useful for italic files made in another font editor

for glyph in font.selection:
	for layer in glyph.layers:
		for anchor in layer.anchors:
			anchor.x -= 38 # units to shift here, change the - by + to move anchors to the right
		for path in layer.paths:
			for node in path.nodes:
				node.x -= 38 # units to shift here, change the - by + to move points to the right
