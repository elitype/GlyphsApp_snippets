# Generates Glyphs App instances

Glyphs.clearLog()
font = Glyphs.font
path = 'pathToSaveInstances'

for instance in font.instances:
	newFont = instance.interpolatedFont
	Glyphs.fonts.append(newFont)
	newFont.save(path + 'MyFamilyName' + instance.name + '.glyphs')
