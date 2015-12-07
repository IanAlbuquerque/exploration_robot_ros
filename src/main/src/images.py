#import skimage.io as skio
import matplotlib.pyplot as plt
import time

#from skimage import img_as_float

last_imshow = None

def createPlot(image):
	global last_imshow
	figure, axe = plt.subplots(ncols=1)
	last_imshow = axe.imshow(image, vmin=0, vmax=1, interpolation="nearest", zorder=0)
	return figure, axe

def plotImage(image,should_block_image=True):
	plt.close()
	createPlot(image)
	plt.show(block = should_block_image)
	if not should_block_image:
		plt.draw()

def readImage(image_path):
	#img = skio.imread(image_path)
	#float_img = img_as_float(img)
	#return float_img
	return None

def updateLastPlot(image):

	last_imshow.set_data(image)
	plt.draw()
	