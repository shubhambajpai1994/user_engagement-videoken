import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import csv
style.use("ggplot")

from sklearn.cluster import KMeans

#print video_values[13][16][1]
video = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_video_hierarchial_without_constraint_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowa in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowa[i]))
        video.append(a)
    #print video
non_video = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_non_video_hierarchial_without_constraint_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowb in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowb[i]))
        non_video.append(a)


colors = ["blue", "yellow", "green", "black", "red", "orange"]
# #############################################################################
# Plot result
for i in range(0,6):
    X=[]
    Y=[]
    for j in range(0,25):
        X.append(video[j][i])
        Y.append(j)
    X.append(0)
    Y.append(26)
    plt.plot(Y,X, color = colors[i])
plt.title("Hierarchial_without_constraint_video")
plt.savefig('/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_hierarchial_without_constraint_video.png')

plt.show()
plt.clf()
for i in range(0,6):
    X=[]
    Y=[]
    for j in range(0,25):
        X.append(non_video[j][i])
        Y.append(j)
    X.append(0)
    Y.append(26)
    plt.plot(Y,X, color = colors[i])
plt.title("Hierarchial_without_constraint_non_video")
plt.savefig('/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_hierarchial_without_constraint_non_video.png')

plt.show()
plt.clf()

