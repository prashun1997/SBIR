import pickle
import cv2
import numpy as np


with open("local.txt", "rb") as fp:  # Unpickling
    local_feature = pickle.load(fp)

with open("global.txt", "rb") as fp:  # Unpickling
    global_feature = pickle.load(fp)

# Extractng features of sketch and fetching the nearest image from the pool of images processed
def fetch():
    img = cv2.imread('my_drawing.jpg', 0)
    edges = cv2.Canny(img, 100, 200)

    hist = [0] * 80
    temp = 0
    for i in range(0, 4):
        for l in range(0, 4):
            for j in range(0, 64, 2):
                for k in range(0, 64, 2):

                    x = j + (i * 64)
                    y = k + (l * 64)

                    p1 = int(edges[x][y])
                    p2 = int(edges[x][y + 1])
                    p3 = int(edges[x + 1][y])
                    p4 = int(edges[x + 1][y + 1])

                    if (((p1 + p3) == 510 and (p2 + p4) == 0) or ((p2 + p4) == 510 and (p1 + p3) == 0)):
                        hist[temp * 5] += 1 / 1024.0
                    if (((p1 + p2) == 510 and (p3 + p4) == 0) or ((p3 + p4) == 510 and (p1 + p2) == 0)):
                        hist[temp * 5 + 1] += 1 / 1024.0
                    if ((p1 + p4) == 510 and (p3 + p2) == 0):
                        hist[temp * 5 + 2] += 1 / 1024.0
                    if ((p1 + p4) == 0 and (p3 + p2) == 510):
                        hist[temp * 5 + 3] += 1 / 1024.0
                    if (p1 + p2 + p3 + p4 == 1020):
                        hist[temp * 5 + 4] += 1 / 1024.0
            temp += 1

    glob = [0] * 5
    for i in range(0, 80):
        glob[i % 5] += hist[i]

    min=10000
    minimum=0
    # Comparing local and global feautures
    for i in range(0,len(local_feature)):
        diff=0
        for j in range(0,len(local_feature[i])):
            diff+=abs(hist[j]-local_feature[i][j])
        for k in range(0,len(global_feature[i])):
            diff+=abs(glob[k]-global_feature[i][k])
        if(diff<min):
            min=diff
            minimum=i

    return minimum

