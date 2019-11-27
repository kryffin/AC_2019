# -*-coding:Latin-1 -*

#author : kleinhentz - gouth
#algo qui résoud le problème de 3,2 SSS

""" 
-------------------------------------
Couleurs :
	R = 0
	V = 1
	B = 2
-------------------------------------
Contraintes binaires représentées par un tableau 4D :

binaire[x][y][2][1] == True

signifie que [(x,2), (y, 1)]
et donc [(x,B), (y,V)]
-------------------------------------
Contrainte unaire représentées oar yb tableau 2D : 

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

argv = sys.argv
if(len(argv)!=2):
	print "\nusage : python 32SSS.py nombreDeVariable\n"
	sys.exit

#on recupere le nombre de variable
N = int(argv[1]) 

print "there is", N , "variables\n"
##déclaration des variables globales##
unaire = np.array([[False] *3 for _ in range(N)])
print "array of", unaire.ndim ,"created"
binaire = np.array(
	[#1st layer
		[[[False]*3 for _ in range(3)]]*N for _ in range(N) 
	])


print "array of", binaire.ndim, "created"

def init():
	#print unaire
	pass


def printUnaire():
	print "====printing unaire=====\n"
	for i in range(0,N):
		print "x",i
		for j in range(3):
			print unaire[i][j]
		print "\n"

def printBinaire():
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



def main():
	global unaire
	global binaire
	#printUnaire()
	unaire[0][1] = True
	#printUnaire()
	binaire[1][2][1][2] = True #x1 = V, x2 = B
	printBinaire()
	init()

if __name__ == "__main__":
    # execute only if run as a script
    main()

