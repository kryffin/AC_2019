# -*-coding:Latin-1 -*

def printUnaire(N, unaire):
	print "====printing unaire=====\n"
	for i in range(0,N):
		for j in range(3):
			if(unaire[i][j]):
				print "x",i , "col,", j
				print unaire[i][j]


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
			res = False
			for c1 in range (0, 3):
				for c2 in range (0, 3):
					if(binaire[i][j][c1][c2]):
						res = res or True
			if(res):
				print binaire[i,j]
			


def init_default1(N, unaire, binaire, var):
	"""
	[(x0,R)], [(x0,B)],
	[(x0,B),(x1,R)], 
	[(x0,R),(x2,B)],
	[(x0,V),(x2,V)], 
	[(x0,B),(x4,R)],
	[(x0,V),(x4,B)], 
	[(x0,B),(x4,V)],
	[(x2,V),(x3,V)], 
	[(x2,B),(x4,R)]
	"""
	unaire[0][0] = True
	unaire[0][2] = True
	binaire[0][1][2][0] = True
	binaire[0][2][0][2] = True
	binaire[0][2][1][1] = True
	binaire[0][4][2][0] = True
	binaire[0][4][1][2] = True
	binaire[0][4][2][1] = True
	binaire[2][3][1][1] = True
	binaire[2][4][2][0] = True


"""
	##output cas 2 :
	[(x0,R)], [(x0,B)],
	[(x1,R)], [(x2,B)], 
	[(x2,V)], [(x4,R)],
	[(x4,B)], [(x4,V)], 
	[(x2,V),(x3,V)],
	[(x2,B),(x4,R)]

"""