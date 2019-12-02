# -*-coding:Latin-1 -*

#author : kleinhentz - gouth
#algo qui résoud le problème de 3,2 SSS

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

	for i in range (0,N):
		if(var[i]==True):
			b1 = (unaire[i][1]==unaire[i][2] and unaire[i][1] == True) #xi,G | xi,B
			b2 = (unaire[i][0]==unaire[i][1] and unaire[i][0] == True) #xi,R | xi,G 
			b3 = (unaire[i][0]==unaire[i][2] and unaire[i][0] == True) #xi,R | xi,B

			"""
			print "++++DEBUG++++"
			print b1
			print b2
			print b3
			print "--------"
			"""
			if(b1 or b2 or b3): #si x_i apparait dans deux contraintes unaires
				print "x", i," appareas to be in two unary constraint...."
				for f in range (0,N): #pour toutes les variables dont le couples s'associe avec xi
					for col_x in range(0,3): #les couleurs de X {R,G,B}
						for col_f in range(0,3): #les couleurs f {R,G,B}
							if(binaire[f][i][col_f][col_x] or binaire[i][f][col_x][col_f]): #si une contrainte binaire existe contenant xi 
								print "changing x",f ," binary constraint into unary contraint..."
								binaire[f][i][col_f][col_x] = False #on supprime les contraintes de type [(y,{R,G,B}), (x_i,{R,G,B})]
								binaire[i][f][col_x][col_f] = False #on supprime les contraintes de type [(x_i,{R,G,B}), (y,{R,G,B})]
								unaire[f][col_f] = True #on ajoute la contrainte unaire [y,{R,G,B}]
					

			


def process():
	Continue = cas1()
	print "cas1 return " , Continue 
	if(Continue):
		cas2()

def main():
	global unaire
	global binaire
	global N
	global var

	#printing.printUnaire(N, unaire)
	#printing.printBinaire(N, binaire)
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

