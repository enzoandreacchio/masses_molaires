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
	output = []
	# Prise du screen
	p.screenshot("straight_to_disk.png")
	# stockage dans une var
	img = cv2.imread("straight_to_disk.png")
	for y in range(1, 9):
		for x in range(1, 9):
			cooX = (346 + x * 113) - 3
			cooY = (1005 - (y-1) * 113) - 3
			if str(img[cooY, cooX]) == "[130 246 246]" or str(img[cooY, cooX]) == "[ 68 202 186]":
				output.append((x, y))
	return output


# fonction qui renvoie les cases de départ et d'arrivée de nouvelle pièce jouée par le joueur
def testMovePlayer():
	output = []

	# Prise du screen
	p.screenshot("straight_to_disk.png")
	# stockage dans une var
	img = cv2.imread("straight_to_disk.png")

	for y in range(1, 9):
		for x in range(1, 9):
			cooX = (316 + x * 113) - 3
			cooY = (1005 - (y-1) * 113) - 3
			if str(img[cooY, cooX]) == "[130 246 246]" or str(img[cooY, cooX]) == "[ 68 202 186]":
				output.append((x, y))
	return output



#détection coup du joueur
print(testMovePlayer())

# vers la page du bot
p.moveTo(361, 13)
p.click()



# détection du coup joué par le bot
print(testMoveBot())





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