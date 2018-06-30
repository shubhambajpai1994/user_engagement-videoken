import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import csv
style.use("ggplot")

from sklearn.cluster import KMeans

#print video_values[13][16][1]
video = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_video_multi_level_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowa in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowa[i]))
        video.append(a)
    #print video
non_video = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_non_video_multi_level_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowb in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowb[i]))
        non_video.append(a)

video1 = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_video_k_mean_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowa in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowa[i]))
        video1.append(a)
    #print video
non_video1 = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_non_video_k_mean_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowb in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowb[i]))
        non_video1.append(a)

video2 = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_video_hierarchial_with_constraint_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowa in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowa[i]))
        video2.append(a)
    #print video
non_video2 = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_non_video_hierarchial_with_constraint_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowb in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowb[i]))
        non_video2.append(a)

video3 = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_video_hierarchial_without_constraint_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowa in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowa[i]))
        video3.append(a)
    #print video
non_video3 = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/mean_non_video_hierarchial_without_constraint_clustering.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowb in csvReader:
        a = []
        for i in range(0, 6):
            a.append(float(rowb[i]))
        non_video3.append(a)


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
    plt.plot(Y,X, color = colors[0])
    X = []
    Y = []
    for j in range(0,25):
        X.append(video1[j][i])
        Y.append(j)
    X.append(0)
    Y.append(26)
    plt.plot(Y,X, color = colors[1])
    X = []
    Y = []
    for j in range(0,25):
        X.append(video2[j][i])
        Y.append(j)
    X.append(0)
    Y.append(26)
    plt.plot(Y,X, color = colors[2])
    X = []
    Y = []
    for j in range(0,25):
        X.append(video3[j][i])
        Y.append(j)
    X.append(0)
    Y.append(26)
    plt.plot(Y,X, color = colors[3])
    plt.title("Clustering_algorithm_video")
    plt.savefig('/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/clustering_compare_video_c'+str(i)+'.png')
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
    plt.plot(Y,X, color = colors[0])
    X = []
    Y = []
    for j in range(0,25):
        X.append(non_video1[j][i])
        Y.append(j)
    X.append(0)
    Y.append(26)
    plt.plot(Y,X, color = colors[1])
    X = []
    Y = []
    for j in range(0,25):
        X.append(non_video2[j][i])
        Y.append(j)
    X.append(0)
    Y.append(26)
    plt.plot(Y,X, color = colors[2])
    X = []
    Y = []
    for j in range(0,25):
        X.append(non_video3[j][i])
        Y.append(j)
    X.append(0)
    Y.append(26)
    plt.plot(Y,X, color = colors[3])
    plt.title("Clustering_algorithm_non_video")
    plt.savefig('/Users/shubham.bajpai/Documents/User_Engagement/source/data_processing/clustering_compare_non_video_c'+str(i)+'.png')
    plt.show()
    plt.clf()

