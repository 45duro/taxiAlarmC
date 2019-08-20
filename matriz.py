matriz_led =[[1 , 2, 3, 4, 5, 6, 7,8],
			[9, 10,11,12,13,14,15,16],
			[17,18,19,20,21,22,23,24],
			[25,26,27,28,29,30,31,32],
			[33,34,35,36,37,38,30,40], 
			[41,42,43,44,45,46,47,48], 
			[49,50,51,52,53,54,55,56], 
			[57,58,59,60,61,62,63,64]]

#para imprimir primera fila en orden


for filas in range(8):
	for colum in range(8):

		if filas == 0:
			print(matriz_led[0][colum])
	
	print(matriz_led[filas][7])

for filas in range(7,-1,-1):
	for colum in range(7,-1,-1):
		if filas == 7:
			print(matriz_led[7][colum])
	
	print(matriz_led[filas][0])