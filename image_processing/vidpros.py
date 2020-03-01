import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from getcolor import *
import pickle

cap = cv2.VideoCapture(0)

#arr = []

colorId = ['green', 'orange', 'white', 'yellow', 'blue', 'red']

#load model
savefile = 'cluster_model.sav'
loaded_model = pickle.load(open(savefile, 'rb'))

while(True):
    ret, frame = cap.read()
    vals, newIm = getColors(frame)
    cv2.imshow('frame', newIm)

    #press p to predict
    if cv2.waitKey(1) & 0xFF == ord('p'):
        #print raw rgb values of the squares
        print(vals)

        """
        #append rgb values to list to act as training data
        for i in range(3):
            for j in range(3):
                arr.append(vals[i][j][:3])
        """

        #use model to predict based on rgb values
        for i in range(3):
            for j in range(3):
                print(colorId[loaded_model.predict([vals[i][j][:3]])[0]])

    #spam q to exit
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

#print(arr)

#close
cap.release()
cv2.destroyAllWindows()




"""
#init model
kmeans = KMeans(n_clusters = 6, init='k-means++', max_iter=300, n_init=10, random_state = 0)
#train model
kmeans.fit(arr)

#display data with centers
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for x in arr:
    ax.scatter(x[0], x[1], x[2], marker='o')

ax.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], kmeans.cluster_centers_[:,2], s=300, c='red')

plt.show()

#save model to be used later
savefile = 'cluster_model.sav'
pickle.dump(kmeans, open(savefile, 'wb'))
"""

#load model
#savefile = 'cluster_model.sav'
#loaded_model = pickle.load(open(savefile, 'rb'))

"""
#testing data, doesn't really work as well as image
print(loaded_model.predict([[255, 0, 0]]))
print(loaded_model.predict([[0, 255, 0]]))
print(loaded_model.predict([[0, 0, 255]]))
print(loaded_model.predict([[0, 255, 255]]))
print(loaded_model.predict([[0, 128, 255]]))
print(loaded_model.predict([[255, 255, 255]]))
"""
