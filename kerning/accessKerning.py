Glyphs.clearLog()
font = Glyphs.font
masterID = 'FE3CAB03-7F98-4468-BF19-2B4A67A15FD3'

for master, kern in font.kerning.items():
	if master == masterID:
		for right, left in kern.items():
			for second, value in left.items():
				if second.startswith('@MMK_R_DEV_dNa_2ND'):
					print(right, second, value) 
