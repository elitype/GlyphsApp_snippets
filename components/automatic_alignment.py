Glyphs.clearLog()
font = Glyphs.font

for glyph in font.selection:
    for layer in glyph.layers:
        for component in layer.components:
            # print(component)
            component.automaticAlignment = True
