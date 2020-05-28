# import the necessary packages
from pyimagesearch.rgbhistogram import RGBHistogram
from imutils.paths import list_images
import argparse
import pickle
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())
# initialize the index dictionary to store our our quantifed
# images, with the 'key' of the dictionary being the image
# filename and the 'value' our computed features
index = {}

# initialize our image descriptor -- a 3D RGB histogram with
# 8 bins per channel
desc = RGBHistogram([8, 8, 8])

for imagePath in list_images(args['dataset']):
    print(imagePath)
    k = imagePath[imagePath.rfind('/')+1:]
    image = cv2.imread(imagePath)
    features = desc.describe(image)
    index[k] = features
f = open(args["index"], "wb")
f.write(pickle.dumps(index))
f.close()

print('[INFO] done....indexed {} images'.format(len(index)))

