Glyphs.clearLog()
font = Glyphs.font

# removes components of selected glyphs
for glyph in font.selection:
	for layer in glyph.layers:
		if layer.name == 'Color 0':
			if layer.components:
				for component in layer.components:
					if component.name.endswith('comb'):
						del component
#						print(component.componentName)
		if layer.name == 'Color 1':
			if layer.components:
				for component in layer.components:
					if component.name.endswith('comb'):
						del component
#						print(component.componentName)
print('Done')
