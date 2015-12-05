import math
import sys
import numpy as np
import skimage.io as skio
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from skimage import img_as_float
from skimage.draw import polygon
from matplotlib.offsetbox import OffsetImage
from matplotlib.offsetbox import AnnotationBbox

MAP_FILE_NAME = "map.jpg"
N = 30
M = 30

DISC_LEN = 32

DIR_WEST = 0
DIR_NORTH = 1
DIR_EAST = 2
DIR_SOUTH = 3

POS_X = 0
POS_Y = 0
DIR = DIR_EAST

discretization = None
last_p = [(None,None),None]
axe = None

"""
player_line = None

def updatePlayer():
	global axe
	global player_line
	print player_line
	if player_line != None:
			axe.lines.remove(player_line)
	player_line = plt.Line2D([POS_X*DISC_LEN,POS_X*DISC_LEN+5],[POS_Y*DISC_LEN,POS_Y*DISC_LEN+5])
	axe.add_line(player_line)
	plt.draw()
"""

"""
player_lines = [None,None,None]

def updatePlayer():
	global axe
	global player_lines
	if player_lines[0] != None:
			for line in player_lines:
				axe.lines.remove(line)

	if DIR == DIR_WEST or DIR == DIR_EAST:
		player_lines[0] = plt.Line2D([POS_X*DISC_LEN,(POS_X+1)*DISC_LEN],[POS_Y*DISC_LEN+DISC_LEN/2,POS_Y*DISC_LEN+DISC_LEN/2])
	elif DIR == DIR_SOUTH or DIR == DIR_NORTH:
		player_lines[0] = plt.Line2D([POS_X*DISC_LEN+DISC_LEN/2,POS_X*DISC_LEN+DISC_LEN/2],[POS_Y*DISC_LEN,(POS_Y+1)*DISC_LEN])

	if DIR == DIR_NORTH:
		player_lines[1] = plt.Line2D([POS_X*DISC_LEN+DISC_LEN/2,(POS_X+1)*DISC_LEN],[POS_Y*DISC_LEN,(POS_Y+1)*DISC_LEN])
		player_lines[2] = plt.Line2D([POS_X*DISC_LEN+DISC_LEN/2,POS_X*DISC_LEN],[POS_Y*DISC_LEN,(POS_Y+1)*DISC_LEN])
	elif DIR == DIR_SOUTH:
		player_lines[1] = plt.Line2D([POS_X*DISC_LEN+DISC_LEN/2,(POS_X+1)*DISC_LEN],[(POS_Y+1)*DISC_LEN,POS_Y*DISC_LEN])
		player_lines[2] = plt.Line2D([POS_X*DISC_LEN+DISC_LEN/2,POS_X*DISC_LEN],[(POS_Y+1)*DISC_LEN,POS_Y*DISC_LEN])
	if DIR == DIR_WEST:
		player_lines[1] = plt.Line2D([POS_X*DISC_LEN,(POS_X+1)*DISC_LEN],[POS_Y*DISC_LEN+DISC_LEN/2,POS_Y*DISC_LEN])
		player_lines[2] = plt.Line2D([POS_X*DISC_LEN,(POS_X+1)*DISC_LEN],[POS_Y*DISC_LEN+DISC_LEN/2,(POS_Y+1)*DISC_LEN])
	if DIR == DIR_EAST:
		player_lines[1] = plt.Line2D([POS_X*DISC_LEN,(POS_X+1)*DISC_LEN],[POS_Y*DISC_LEN,POS_Y*DISC_LEN+DISC_LEN/2])
		player_lines[2] = plt.Line2D([POS_X*DISC_LEN,(POS_X+1)*DISC_LEN],[(POS_Y+1)*DISC_LEN,POS_Y*DISC_LEN+DISC_LEN/2])

	for line in player_lines:
		axe.add_line(line)
	plt.draw()
"""


east_img = skio.imread("right.jpg")
west_img = skio.imread("left.jpg")
north_img = skio.imread("up.jpg")
south_img = skio.imread("down.jpg")
player_artist = None
def updatePlayer():
	global axe
	global player_artist
	if player_artist:
		axe.artists.remove(player_artist)

	if DIR == DIR_NORTH:
		im = OffsetImage(north_img, zoom=0.5)
		player_artist = AnnotationBbox(im, (POS_X*DISC_LEN+16,POS_Y*DISC_LEN+16), xycoords='data', frameon=False)
		axe.add_artist(player_artist)
	elif DIR == DIR_SOUTH:
		im = OffsetImage(south_img, zoom=0.5)
		player_artist = AnnotationBbox(im, (POS_X*DISC_LEN+16,POS_Y*DISC_LEN+16), xycoords='data', frameon=False)
		axe.add_artist(player_artist)
	if DIR == DIR_WEST:
		im = OffsetImage(west_img, zoom=0.5)
		player_artist = AnnotationBbox(im, (POS_X*DISC_LEN+16,POS_Y*DISC_LEN+16), xycoords='data', frameon=False)
		axe.add_artist(player_artist)
	if DIR == DIR_EAST:
		im = OffsetImage(east_img, zoom=0.5)
		player_artist = AnnotationBbox(im, (POS_X*DISC_LEN+16,POS_Y*DISC_LEN+16), xycoords='data', frameon=False)
		axe.add_artist(player_artist)

	plt.draw()

def onKeyPress(event):
	global DIR_WEST
	global DIR_NORTH
	global DIR_EAST
	global DIR_SOUTH

	global POS_X
	global POS_Y
	global DIR

	if event.key == 'w' or event.key == 'W':
		print "Hey"
		if DIR == DIR_WEST:
			POS_X = POS_X - 1
		elif DIR == DIR_NORTH:
			POS_Y = POS_Y - 1
		elif DIR == DIR_EAST:
			POS_X = POS_X + 1
		elif DIR == DIR_SOUTH:
			POS_Y = POS_Y + 1
	elif event.key == 's' or event.key == 'S':
		if DIR == DIR_WEST:
			POS_X = POS_X + 1
		elif DIR == DIR_NORTH:
			POS_Y = POS_Y + 1
		elif DIR == DIR_EAST:
			POS_X = POS_X - 1
		elif DIR == DIR_SOUTH:
			POS_Y = POS_Y - 1
	elif event.key == 'a' or event.key == 'A':
		if DIR == DIR_WEST:
			DIR = DIR_SOUTH
		elif DIR == DIR_NORTH:
			DIR = DIR_WEST
		elif DIR == DIR_EAST:
			DIR = DIR_NORTH
		elif DIR == DIR_SOUTH:
			DIR = DIR_EAST
	elif event.key == 'd' or event.key == 'D':
		if DIR == DIR_WEST:
			DIR = DIR_NORTH
		elif DIR == DIR_NORTH:
			DIR = DIR_EAST
		elif DIR == DIR_EAST:
			DIR = DIR_SOUTH
		elif DIR == DIR_SOUTH:
			DIR = DIR_WEST

	print (POS_X,POS_Y)

	updatePlayer()


if __name__ == '__main__':

	place_map = skio.imread(MAP_FILE_NAME)
	discretization = np.zeros([M*DISC_LEN,N*DISC_LEN,3])

	W = place_map.shape[1]
	H = place_map.shape[0]
	W_STEP = float(W)/N
	H_STEP = float(H)/M

	figure, axes = plt.subplots(ncols=3)
	axes[0].imshow(place_map, vmin=0, vmax=1, interpolation="nearest")
	axes[1].imshow(place_map, vmin=0, vmax=1, interpolation="nearest")
	axes[2].imshow(discretization, vmin=0, vmax=1, interpolation="nearest")

	for i in range(1,N):
		line = plt.Line2D([i*W_STEP,i*W_STEP],[0,H])
		axes[1].add_line(line)
	for j in range(1,M):
		line = plt.Line2D([0,W],[j*H_STEP,j*H_STEP])
		axes[1].add_line(line)

	for i in range(0,N):
		for j in range(0,M):
			if 0 in place_map[i*W_STEP:(i+1)*W_STEP,j*H_STEP:(j+1)*H_STEP]:
				discretization[i*DISC_LEN:(i+1)*DISC_LEN,j*DISC_LEN:(j+1)*DISC_LEN] = 0
			else:
				discretization[i*DISC_LEN:(i+1)*DISC_LEN,j*DISC_LEN:(j+1)*DISC_LEN] = 1

	plt.show()

	figure, axe = plt.subplots(ncols=1)
	axe.imshow(discretization, vmin=0, vmax=1, interpolation="nearest", zorder=0)

	listener_key_press = figure.canvas.mpl_connect('key_press_event', onKeyPress)

	for i in range(1,N):
		line = plt.Line2D([i*DISC_LEN,i*DISC_LEN],[0,M*DISC_LEN])
		axe.add_line(line)
	for j in range(1,M):
		line = plt.Line2D([0,N*DISC_LEN],[j*DISC_LEN,j*DISC_LEN])
		axe.add_line(line)

	updatePlayer()

	plt.show()
	plt.draw()


