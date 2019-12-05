# -*-coding:Latin-1 -*

def intToCol(x):
	if x == 0:
		return "R"
	if x == 1:
		return "G"
	if x == 2:
		return "B"


def printConstraint(var, col):
	print "[(x",var,",",intToCol(col),")]"

def printUnaire(N, unaire):
	print "====printing unaire=====\n"
	for i in range(0,N):
		for j in range(3):
			if(unaire[i][j]):
				print "[(x",i,",",intToCol(j),")]"


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
			res = False
			for c1 in range (0, 3):
				for c2 in range (0, 3):
					if(binaire[i][j][c1][c2]):
						print "[(x",i,",",intToCol(c1),"),(x",j,",",intToCol(c2),")]"


def afficherVar(N, var):
	for i in range (0,N):
		print "x",i ,"=",var[i]

def init_default1(N, unaire):
	### utilisé pour tester le cas 1
	"""
	[(x0,R)], [(x0,G)], [(x0,B)]
	"""

	unaire[0][0] = True
	unaire[0][1] = True
	unaire[0][2] = True
	
	#excpected ouput : FALSE

def init_zero(N, unaire, binaire, var):
	for i in range (0,N):
		var[i] = True
		unaire[i][0] = False
		unaire[i][1] = False
		unaire[i][2] = False
		for j in range (0,N):
			for col1 in range (0,3):
				for col2 in range (0,3):
					binaire[i][j][col1][col2] = False

def init_default2(N, unaire, binaire, var):
	### utilisé pour tester le cas 2
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
	[(x0,R)], 
	[(x0,B)],
	[(x1,R)], 
	[(x2,B)], 
	[(x2,V)], 
	[(x4,R)],
	[(x4,B)], 
	[(x4,V)], 
	[(x2,V),(x3,V)],
	[(x2,B),(x4,R)]

"""

def init_default3(N, unaire, binaire, var):
	### utilisé pour tester le cas 3

	"""
	[(x0,R)],

	[(x0,R),(x1,V)]
	[(x0,R),(x1,B)]

	[(x0,B),(x1,R)], 
	[(x0,V),(x2,B)],

	[(x0,V),(x2,V)], 
	[(x0,B),(x4,R)],
	
	[(x0,V),(x4,B)], 
	[(x0,B),(x4,V)],
	 
	"""
	unaire[0][0] = True
	binaire[0][1][0][1] = True
	binaire[0][1][0][2] = True

	binaire[0][1][2][0] = True
	binaire[0][2][1][2] = True

	binaire[0][2][1][1] = True
	binaire[0][4][2][0] = True
	
	binaire[0][4][1][2] = True
	binaire[0][4][2][1] = True
	

"""
	##output cas 3 :
	[(x0,R)], 

	[(x0,B),(x1,R)], 
	[(x0,V),(x2,B)],

	[(x0,V),(x2,V)], 
	[(x0,B),(x4,R)],
	
	[(x0,V),(x4,B)], 
	[(x0,B),(x4,V)],
	
new	[(x1,R)], [(x2,B)], 

new	[(x2,V)], [(x4,R)],
	
new	[(x4,B)], [(x4,V)]

"""