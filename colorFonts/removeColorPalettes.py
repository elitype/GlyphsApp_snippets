Glyphs.clearLog()
docs = Glyphs.documents
font = doc.font
# Removes color palettes for a specific project, needs to be adjusted
for doc in docs:
	for instance in doc.font.instances:
		for param in instance.customParameters:
			if param.name == 'Color Palette for CPAL':
				param.value = 0
	print('Adjusted CPAL values to 0')

	for instance in doc.font.instances:
		color_palettes = doc.font.customParameters['Color Palettes']
		violet = 0
		indigo = 1
		blue = 2
		green = 3
		yellow = 4
		orange = 5
		red = 6
		if instance.name == 'Violet':
			del color_palettes[red]
			del color_palettes[orange]
			del color_palettes[yellow]
			del color_palettes[green]
			del color_palettes[blue]
			del color_palettes[indigo]
		elif instance.name == 'Indigo':
			print('Instance {}' .format(instance.name))
			del color_palettes[red]
			del color_palettes[orange]
			del color_palettes[yellow]
			del color_palettes[green]
			del color_palettes[blue]
			del color_palettes[violet]
		elif instance.name == 'Blue':
			print('Instance {}' .format(instance.name))
			del color_palettes[red]
			del color_palettes[orange]
			del color_palettes[yellow]
			del color_palettes[green]
			del color_palettes[indigo]
			del color_palettes[violet]
		elif instance.name == 'Green':
			print('Instance {}' .format(instance.name))
			del color_palettes[red]
			del color_palettes[orange]
			del color_palettes[yellow]
			del color_palettes[blue]
			del color_palettes[indigo]
			del color_palettes[violet]
		elif instance.name == 'Yellow':
			print('Instance {}' .format(instance.name))
			del color_palettes[red]
			del color_palettes[orange]
			del color_palettes[green]
			del color_palettes[blue]
			del color_palettes[indigo]
			del color_palettes[violet]	
		elif instance.name == 'Orange':
			print('Instance {}' .format(instance.name))
			del color_palettes[red]
			del color_palettes[yellow]
			del color_palettes[green]
			del color_palettes[blue]
			del color_palettes[indigo]
			del color_palettes[violet]	
		elif instance.name == 'Red':
			print('Instance {}' .format(instance.name))
			del color_palettes[orange]
			del color_palettes[yellow]
			del color_palettes[green]
			del color_palettes[blue]
			del color_palettes[indigo]
			del color_palettes[violet]
		elif instance.name == 'Mono':
			pass
	print('Adjusted color palettes in instances')
