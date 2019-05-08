import numpy as np
import pyautogui as p
import imutils
import cv2
import keyboard
import time
from math import *



p.moveTo(563, 1064)
p.click()
p.moveTo(50, 11)
p.click()

# Prise du screen
p.screenshot("straight_to_disk.png")
# stockage dans une var
img = cv2.imread("straight_to_disk.png")



# fonction qui renvoie les cases de départ et d'arrivée de nouvelle pièce jouée par le bot
def testMoveBot():
	# Prise du screen
	p.screenshot("straight_to_disk.png")
	# stockage dans une var
	img = cv2.imread("straight_to_disk.png")

	output = [(0, 0), (0, 0)]
	for y in range(1, 9):
		for x in range(1, 9):
			cooX = (346 + x * 113) - 3
			cooY = (1005 - (y-1) * 113) - 3
			if str(img[cooY, cooX]) == "[130 246 246]" or str(img[cooY, cooX]) == "[ 68 202 186]":
				x_test = cooX
				incr = 0
				while x_test >= cooX - 107:
					if str(img[cooY - 50, x_test]) != "[130 246 246]" and str(img[cooY - 50, x_test]) != "[ 68 202 186]":
						incr = 1
					x_test -= 1

				if incr == 1:
					output[1] = (x, y)
				else:
					output[0] = (x, y)
				
	return output


# fonction qui renvoie les cases de départ et d'arrivée de nouvelle pièce jouée par le joueur
def testMovePlayer():

	# Prise du screen
	p.screenshot("straight_to_disk.png")
	# stockage dans une var
	img = cv2.imread("straight_to_disk.png")

	output = [(0, 0), (0, 0)]
	for y in range(1, 9):
		for x in range(1, 9):
			cooX = (316 + x * 113) - 3
			cooY = (1005 - (y-1) * 113) - 3
			if str(img[cooY, cooX]) == "[130 246 246]" or str(img[cooY, cooX]) == "[ 68 202 186]":
				x_test = cooX
				incr = 0
				while x_test >= cooX - 107:
					if str(img[cooY - 50, x_test]) != "[130 246 246]" and str(img[cooY - 50, x_test]) != "[ 68 202 186]":
						incr = 1
					x_test -= 1

				if incr == 1:
					output[1] = (x, y)
				else:
					output[0] = (x, y)
	return output



def play_bot(coup):
	coup = [(9-coup[0][0], 9-coup[0][1]), (9-coup[1][0], 9-coup[1][1])]
	print(coup)
	p.click(402 + (coup[0][0] - 1) * 113, 949 - (coup[0][1] - 1) * 113)
	p.click(402 + (coup[1][0] - 1) * 113, 949 - (coup[1][1] - 1) * 113)

def play_player(coup):
	coup = [(9-coup[0][0], 9-coup[0][1]), (9-coup[1][0], 9-coup[1][1])]
	print(coup)
	p.click(372 + (coup[0][0] - 1) * 113, 949 - (coup[0][1] - 1) * 113)
	p.click(372 + (coup[1][0] - 1) * 113, 949 - (coup[1][1] - 1) * 113)



	



# détection coup du joueur
coup = testMovePlayer()
print(coup)

# vers la page du bot
p.click(361, 13)

# jeu contre le bot
play_bot(coup)
# attente de la réponse du bot
time.sleep(5)

# détection coup de bot
coup = testMoveBot()
print(coup)

# vers la page du player
p.click(111, 13)

# jeu contre le player
play_player(coup)











"""
# Affichage de l'image
cv2.imshow("test", imutils.resize(img, width = 1500))
cv2.waitKey(0)
cv2.destroyAllWindows()
"""










"""
Peindre la case c7 en blanc
img[214:327, 572:685] = [255, 255, 255]

colorer le pixel (100, 103) en blanc 
img[103, 100] = [255, 255, 255]


dimensions : (101:1005, 346:1250)
côté de l'échiquier : 904
côté d'une case : 113 
"""