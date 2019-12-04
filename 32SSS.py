# -*-coding:Latin-1 -*

#author : kleinhentz - gouth
#algo qui résoud le problème de 3-COLORATION via une reduction au problème (3,2)SSS

""" 
-------------------------------------
Couleurs :
	R = 0
	G = 1
	B = 2
-------------------------------------
Contraintes binaires représentées par un tableau 4D :

binaire[x][y][2][1] == True

signifie que [(x,2), (y, 1)]
et donc [(x,B), (y,V)]
-------------------------------------
Contrainte unaire représentées par un tableau 2D : 

unaire[x][2] == True

signifie que [(x,2)]
et donc [(x,B)]
-------------------------------------
de ce fait nos tableaux "binaire" et "unaire" contienne des booléens
et capture l'ensemble des contraintes possibles pour N variable
unaire[N][{0,1,2}]
binaire[N][N][{0,1,2}][{0,1,2}]
-------------------------------------
Representer les variables :
var[N] == True

signifie que la variable x_N est encore dans l'algo,
si var[i] == False, pour tout i, jusqu'à N, alors l'algo renvoie VRAI

si l'algo aboutit à une contradiction, l'algo envoie NON 

"""
import sys
import numpy as np
import printing


argv = sys.argv
if(len(argv)!=2):
	print "\nusage : python 32SSS.py nombreDeVariable\n"
	sys.exit()

#on recupere le nombre de variable
N = int(argv[1]) 

var = np.array([True] * N) #1 dimension
print "array of ", N , "variables created"

##TABLEAU UNAIRE GLOBAL##
unaire = np.array([[False] *3 for _ in range(N)]) #2 dimensions
print "array of", unaire.ndim ,"dimensions created for unary constraint"
#unaire[0][1] = True  ==> x0 = V

##TABLEAU BINAIRE GLOBAL##
binaire = np.array(
	[#1st layer
		[[[False]*3 for _ in range(3)]]*N for _ in range(N) #2nd layer continent une matrice pour chaque case
	]) #4 dimensions
print "array of", binaire.ndim, "dimensions created for binary constraint"

def init():
	#print unaire
	pass


def cas1():
	global N #on recupere la variable globale N
	global unaire 
	global var

	print "\n\t==initalize case 1 ...==\n"
	#cas 1 : une variable x apparait dans trois contraintes unaire différentes
	#[(x,R)],[(x,V)] et [(x,B)]
	for i in range (0,N):
		if(var[i]==True):#si on doit process la variable
			if (unaire[i][0]==unaire[i][1] and 
			unaire[i][1]==unaire[i][2] and 
			unaire[i][2]==True): #si il a trois contraintes unaire de x
				print "x_",i," is not satisfiable"
				return False #on repond non
	return True#on repond oui 

def cas2():
	global N #on recupere la variable globale N
	global unaire
	global binaire 
	global var

	res = False

	print "\n\t==initalize case 2 ...==\n"
	for i in range (0,N):
		if(var[i]==True):
			b1 = (unaire[i][1]==unaire[i][2] and unaire[i][1] == True) #xi,G | xi,B
			b2 = (unaire[i][0]==unaire[i][1] and unaire[i][0] == True) #xi,R | xi,G 
			b3 = (unaire[i][0]==unaire[i][2] and unaire[i][0] == True) #xi,R | xi,B

			if(b1 or b2 or b3): #si x_i apparait dans deux contraintes unaires
				res = True #le cas2 a fonctionné on renverra True
				print "\nx", i," appareas to be in two unary constraint...."
				for f in range (0,N): #pour toutes les variables dont le couples s'associe avec xi
					for col_x in range(0,3): #les couleurs de X {R,G,B}
						for col_f in range(0,3): #les couleurs f {R,G,B}
							if(binaire[f][i][col_f][col_x] or binaire[i][f][col_x][col_f]): #si une contrainte binaire existe contenant xi								print "\tchanging x",f ," binary constraint into unary contraint..."
								binaire[f][i][col_f][col_x] = False #on supprime les contraintes de type [(y,{R,G,B}), (x_i,{R,G,B})]
								binaire[i][f][col_x][col_f] = False #on supprime les contraintes de type [(x_i,{R,G,B}), (y,{R,G,B})]
								unaire[f][col_f] = True #on ajoute la contrainte unaire [y,{R,G,B}]

			print "removing x",i,"from variables"
			var[i] = False #on enlève x_i des variables à process
			break #evite de faire le cas 2 pour toutes les variables

	return res
					

def cas3():
	global N
	global unaire
	global binaire
	global var

	res = False
	
	print "\n\t==initalize case 3 ...==\n"
	#x apparait dans une contrainte unaire dans ce cas on remplace 
	#Enlever toutes les contraintes de la forme[(x,R),(y,·)] ou [(y,·),(x,R)]
	#Pour tout couple de contraintes[(x,V),(y,b)]et[(x,B),(z,c)],ajouter la contrainte [(y,b),(z,c)]
	for i in range(0,N):
		if (var[i]): #on doit check encore la variable x_i
			for col_X1 in range (0,3):
				if (unaire[i][col_X1]): #x apparait dans une variable unaire de couleur {R, G ou B}
					res = True #le cas3 a fonctionner en renverra True
					print "\nx",i,"appareas to be in one unary constraint"
					for X2 in range (0,N):
						for col_X2 in range (0,3):

							if(binaire[i][X2][col_X1][col_X2]):
								print "\tremoving binary where x",i,"col:",printing.intToCol(col_X1)," and x",X2," col:",printing.intToCol(col_X2),"...."
								binaire[i][X2][col_X1][col_X2] = False
								if(not binaire[i][X2][col_X1][col_X2]):
									print "\t\t..done"

							if(binaire[X2][i][col_X2][col_X1]):
								print "\tremoving binary where x",i,"col:",printing.intToCol(col_X1)," and x",X2," col:",printing.intToCol(col_X2),"...."
								binaire[X2][i][col_X2][col_X1] = False
								if(not binaire[X2][i][col_X2][col_X1]):
									print "\t\t..done"

							#endif
						#endfor
					#endfor
					

					###ici on a enlever toutes les contraintes de la forme[(x,R),(y,·)] ou [(y,·),(x,R)] 
					#fin for X2 in range (0,N):
					
					#si col_X1 = R ==> autre_couleur1 = G, autre_couleur2 = B
					#de meme si V ==> R et B
					#si B ==> R et G
					autre_couleur1 = (col_X1 + 1) % 3
					autre_couleur2 = (col_X1 + 2) % 3

					print "\nsetting new binary constraints..."
					for Y in range (0,N):
						for Z in range (0,N):
							for color_Y in range (0,3):
								for color_Z in range (0,3):
									
									#si [(x,R)] , b1 = true si il existe une contrainte binaire 
									#[(x,V),(y,{R,G,B})] et [(x,B), (z, {R,G,B})]
									
									#si [(x,R)], b2 = true si il existe une contrainte binaire
									#[(x,B), (y,{R,G,B})] et [(x,V), (z, {R,G,B})]
									b1 = (binaire[i][Y][autre_couleur1][color_Y] and binaire[i][Z][autre_couleur2][color_Z])
									b2 = (binaire[i][Y][autre_couleur2][color_Y] and binaire[i][Z][autre_couleur1][color_Z])
									
									#######################
									#
									#	NE VRAIMENT PAS ENLEVER LA CONTRAINTE 
									#	[(x,B), (y,{R,G,B})] et [(x,V), (z, {R,G,B})] 
									# 
									#	????
									#
									#######################
									if(b1 or b2):
										print "\tadding constraint where x", Y,", ", printing.intToCol(color_Y), " and x", Z," ,", printing.intToCol(color_Z),"...."
										binaire[Y][Z][color_Y][color_Z] = True
										binaire[Z][Y][color_Z][color_Y] = True

			print "removing x",i,"from variables"
			var[i] = False #on enlève x_i des variables à process
			break #evite de faire le cas3 pour toutes les variables i
	return res
									
								

def cas4():
	pass
								   

def process():
	global N
	global var
 
	while(not all(x == False for x in var)): #tant qu'il y a des variables à process
		if(not cas1()):
			print "==> not satisfiable\n\nExiting...."
			sys.exit()
		if(cas2()):
			continue
		if(cas3()):
			continue

	
	
	print "satisfiable"

def main():
	global unaire
	global binaire
	global N
	global var

	print "initialisation...."
	printing.init_default1(N, unaire, binaire, var)

	print "done\n\nprocessing......"
	process()

	print "done"

	printing.printUnaire(N, unaire)
	printing.printBinaire(N, binaire)

if __name__ == "__main__":
	# execute only if run as a script
	main()

