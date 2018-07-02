import cv2
import numpy as np
from matplotlib import pyplot as plt
import pickle

np.set_printoptions(threshold=np.nan)
local_feature=[]
global_feature=[]

# Looping through all the images contained in the sample_images for taking out the features
for pic in range(0,6):# Change the number of loops according to the images in the folder
    img = cv2.imread('sample_images/'+str(pic)+'.png', 0)
    # Extracting edges of every image through Canny based edge detection algorithm
    edges = cv2.Canny(img, 100, 200)
    # Creating 80 histogram bins to store different feature values based on edge classification
    hist = [0] * 80
    temp = 0


    # Calculating local features by dividing images into sub-images
    for i in range(0, 4):
        for l in range(0, 4):
            for j in range(0, 64, 2):
                for k in range(0, 64, 2):
                    # print j+(i*64), k+(l*64)
                    x = j + (i * 64)
                    y = k + (l * 64)
                    # print x,y
                    p1 = int(edges[x][y])
                    p2 = int(edges[x][y + 1])
                    p3 = int(edges[x + 1][y])
                    p4 = int(edges[x+1][y + 1])

                    # Checking for the different kinds of edges in sub images of an image
                    if (((p1 + p3) == 510 and (p2 + p4) == 0) or ((p2 + p4) == 510 and (p1 + p3) == 0)):
                        hist[temp * 5] += 1/1024.0
                    if (((p1 + p2) == 510 and (p3 + p4) == 0) or ((p3 + p4) == 510 and (p1 + p2) == 0)):
                        hist[temp * 5 + 1] += 1/1024.0
                    if ((p1 + p4) == 510 and (p3 + p2) == 0):
                        hist[temp * 5 + 2] += 1/1024.0
                    if ((p1 + p4) == 0 and (p3 + p2) == 510):
                        hist[temp * 5 + 3] += 1/1024.0
                    if (p1 + p2 + p3 + p4 == 1020):
                        hist[temp * 5 + 4] += 1/1024.0
            temp += 1

    glob = [0] * 5
    # Calculating global features by adding all local features of each kind of edge
    for i in range(0, 80):
        glob[i%5]+=hist[i]
    local_feature.append(hist)
    global_feature.append(glob)

with open("local.txt", "wb") as fp:  # Pickling the local features of all images in a file
    pickle.dump(local_feature, fp)

with open("global.txt", "wb") as fp:  # Pickling the global features of all images in a different file
    pickle.dump(global_feature, fp)


