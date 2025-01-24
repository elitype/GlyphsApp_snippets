# Adjusts sidebearings an specific amount of units
Glyphs.clearLog()
font = Glyphs.font

for glyph in font.selection:
    for layer in glyph.layers:
    	print(layer.name, layer.parent.name, layer.LSB)
    	print(layer.name, layer.parent.name, layer.RSB)
    	layer.LSB -= 75
    	layer.RSB -= 75
