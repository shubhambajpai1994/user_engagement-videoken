# Authors : Vincent Michel, 2010
#           Alexandre Gramfort, 2010
#           Gael Varoquaux, 2010
# License: BSD 3 clause

print(__doc__)
from matplotlib import style
style.use("ggplot")
import time as time
import numpy as np
import json
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# #############################################################################
count=0
with open("C:/Users/shubh/PycharmProjects/User_Engagement/source/data_clean/userid_timespent.json") as json_data:
    x = json.load(json_data)
    video = []
    max_videos = 0.0
    max_times = 0.0
    for feature in x:
        videos = 0.0
        times = 0.0
        for key in x[feature].keys():
            # print x[feature][key]
            videos += 1
            times += float(x[feature][key])
        if max_videos<videos:
            max_videos=videos
        if max_times<times:
            max_times=times
        video.append([int(feature), videos, times])
        # print feature
        # print videos
        # print time
# print video
video.sort()
for change_data in video:
    change_data[1] = change_data[1]/max_videos
    change_data[2] = change_data[2] / max_times
assignment=[]
with open("C:/Users/shubh/PycharmProjects/User_Engagement/source/Data_Extraction/assignment/Assignment_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowa in csvReader:
        count+=1
        a = []
        for i in range(0, 25):
            a.append(float(rowa[i]))
        assignment.append(a)
        #print assignment
phrase_cloud = []
with open("C:/Users/shubh/PycharmProjects/User_Engagement/source/Data_Extraction/phrase_cloud/phrase_cloud_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowpc in csvReader:
        a = []
        for i in range(0, 25):
            a.append(float(rowpc[i]))
        phrase_cloud.append(a)
        #print phrase_cloud
discussion = []
with open("C:/Users/shubh/PycharmProjects/User_Engagement/source/Data_Extraction/discussion/discussion_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowd in csvReader:
        a = []
        for i in range(0, 25):
            a.append(float(rowd[i]))
            discussion.append(a)
        #print discussion
mmtoc = []
with open("C:/Users/shubh/PycharmProjects/User_Engagement/source/Data_Extraction/mmtoc/mmtoc_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowm in csvReader:
        a = []
        for i in range(0, 25):
            a.append(float(rowm[i]))
        mmtoc.append(a)
        #print mmtoc
quiz_start = []
with open("C:/Users/shubh/PycharmProjects/User_Engagement/source/Data_Extraction/quiz_data_extract/quiz_start_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowqs in csvReader:
        a = []
        for i in range(0, 25):
            a.append(float(rowqs[i]))
            quiz_start.append(a)
        #print quiz_start
quiz_submit = []
with open("C:/Users/shubh/PycharmProjects/User_Engagement/source/Data_Extraction/quiz_data_extract/quiz_submit_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowq in csvReader:
        a = []
        for i in range(0, 25):
            a.append(float(rowq[i]))
            quiz_submit.append(a)
        #print quiz_submit
#[[1,2],[5,8],[1.5,1.8],[1,0.6],[9,11],[12,10],[1,15]]
week_data = []
for i in range(0, 25):
    week_data.append([])
for user in range(0, count):
    for i in range(0, 25):
        val1 = ((5*float(assignment[user][i]))+float(quiz_start[user][i])+(2.0*float(quiz_submit[user][i])))
        val2 = (float(discussion[user][i])+float(mmtoc[user][i])+float(phrase_cloud[user][i]))
        val2=val2+val1
        val1 = video[user][1]+video[user][2]
        week_data[i].append([val1, val2])
centroid_set = []
for j in range(0, 25):
    centroid_set.append([])
for j in range(15, 40):
    X = np.array(week_data[j-15])
# #############################################################################
# Compute clustering
    print("Compute unstructured hierarchical clustering...")
    st = time.time()
    ward = AgglomerativeClustering(n_clusters=6, linkage='ward').fit(X)
    elapsed_time = time.time() - st
    labels = ward.labels_
    print("Elapsed time: %.2fs" % elapsed_time)
    print("Number of points: %i" % labels.size)

# #############################################################################
# Plot result
    colors = ["y.", "r.", "g.", "b.", "m.", "k."]

    for i in range(len(X)):
   #print ("coordinate:" , X[i], "label:", labels[i])
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

    plt.savefig("C:\Users\shubh\PycharmProjects\User_engagement\hierarchial_cluster_plot\cluster_without_constraint_"+str(j)+".png")
    plt.title('Without connectivity constraints (time %.2fs)' % elapsed_time)
    plt.show()
    plt.clf()


# #############################################################################
# Define the structure A of the data. Here a 10 nearest neighbors
from sklearn.neighbors import kneighbors_graph
for j in range(15, 40):
    X = np.array(week_data[j-15])
    connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)

# #############################################################################
# Compute clustering
    print("Compute structured hierarchical clustering...")
    st = time.time()
    ward = AgglomerativeClustering(n_clusters=6, connectivity=connectivity,
                               linkage='ward').fit(X)
    elapsed_time = time.time() - st
    labels = ward.labels_
    print("Elapsed time: %.2fs" % elapsed_time)
    print("Number of points: %i" % labels.size)

# #############################################################################
# Plot result
    colors = ["y.", "r.", "g.", "b.", "m.", "k."]

    for i in range(len(X)):
   #print ("coordinate:" , X[i], "label:", labels[i])
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

    plt.savefig("C:\Users\shubh\PycharmProjects\User_engagement\hierarchial_cluster_plot\cluster_with_constraint_"+str(j)+".png")
    plt.title('Without connectivity constraints (time %.2fs)' % elapsed_time)
    plt.show()
    plt.clf()