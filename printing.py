# -*-coding:Latin-1 -*

def printUnaire(N, unaire):
	print "====printing unaire=====\n"
	for i in range(0,N):
		print "x",i
		for j in range(3):
			print unaire[i][j]
		print "\n"

def printBinaire(N, binaire):
	"""
		affichage explication : 
		binaire[x1][x2][COLOR1][COLOR2]
		
		(x**1**, x**2**)
						  COLOR2
					   		|
					   		v
				0	 1	    2  
		  0	[[True False False]
COLOR1--> 1	[False False **True**]
		  2	[False False False]]  
			
		pour binaire[1][2][1][2]

		revient à la TDV
		x1 x2	isSet
		R  R    True
		R  V    False
		R  B    False
		V  R    False
		V  V    False
		V  B    True
		B  R    False
		B  V    False
		B  B    False
	"""
	print "====printing binaire=====\n"

	for i in range(N):
		for j in range(N):
			print "(x",i,"x",j,")"
			print binaire[i,j]
			print"\n"

