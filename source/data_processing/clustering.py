import numpy as np
import matplotlib.pyplot as plt
import json
import datetime
from matplotlib import style
import csv
style.use("ggplot")

from sklearn.cluster import KMeans
count=0
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/Data_Extraction/video_process/user_id_daywise_timespent.json") as json_data:
    x = json.load(json_data)
    user_data = {}
    max_videos={}
    max_time={}
    for i in range(15,40):
        max_videos[i] = 1.0
        max_time[i] = 1.0
    for feature in x:
        video = {}
        for i in range(15, 40):
            video[i] =[0,0]
        for days in x[feature].keys():
            year = days[:4]
            month = days[5:7]
            day = days[8:]
            #print year
            dt = datetime.date(int(year), int(month), int(day))
            week_number = dt.isocalendar()[1]
            if year == '2017' and week_number < 40:
                if week_number in video:
                    videos = 0.0
                    time = 0.0
                    for key in x[feature][days].keys():
                        # print x[feature][key]
                        videos += 1
                        time += float(x[feature][days][key])
                        #print time, videos
                    if max_videos[week_number]<videos:
                        max_videos[week_number]=videos
                    if max_time[week_number]<time:
                        max_time[week_number]=time
                video[week_number] = [videos, time]
        user_data[feature]=video
    Z1=sorted(user_data.keys())
    sorted_videos=[]
    for index in Z1:
        sorted_videos.append(user_data[index])
        #print index,user_data[index]
video_values=[]
for change_data in sorted_videos:
    for i in range(15, 40):
        change_data[i][0] = change_data[i][0]/max_videos[i]
        change_data[i][1] = change_data[i][1] / max_time[i]
    video_values.append(change_data)
#print video_values[13][16][1]
assignment=[]
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/Data_Extraction/assignment/Assignment_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowa in csvReader:
        count+=1
        a = []
        for i in range(0, 25):
            a.append(float(rowa[i]))
        assignment.append(a)
        #print assignment
phrase_cloud = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/Data_Extraction/phrase_cloud/phrase_cloud_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowpc in csvReader:
        a = []
        for i in range(0, 25):
            a.append(float(rowpc[i]))
        phrase_cloud.append(a)
        #print phrase_cloud
discussion = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/Data_Extraction/discussion/discussion_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowd in csvReader:
        a = []
        for i in range(0, 25):
            a.append(float(rowd[i]))
            discussion.append(a)
        #print discussion
mmtoc = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/Data_Extraction/mmtoc/mmtoc_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowm in csvReader:
        a = []
        for i in range(0, 25):
            a.append(float(rowm[i]))
        mmtoc.append(a)
        #print mmtoc
quiz_start = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/Data_Extraction/quiz_data_extract/quiz_start_user_data1.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for rowqs in csvReader:
        a = []
        for i in range(0, 25):
            a.append(float(rowqs[i]))
            quiz_start.append(a)
        #print quiz_start
quiz_submit = []
with open("/Users/shubham.bajpai/Documents/User_Engagement/source/Data_Extraction/quiz_data_extract/quiz_submit_user_data1.csv") as csvDataFile:
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
        val2 = val1+val2
        #print val1, val2
        val1 = (2*video_values[user][i+15][0])+video_values[user][i+15][1]
        week_data[i].append([val1, val2])
centroid_set = []
for j in range(0, 25):
    centroid_set.append([])
# #############################################################################
# Compute clustering
for j in range(15, 40):
    X = np.array(week_data[j-15])
    #print X
    kmeans = KMeans(n_clusters=6)
    kmeans.fit(X)

    centroid = kmeans.cluster_centers_
    labels = kmeans.labels_

    #print (centroid)
    centroid_set[j-15]=centroid
    with open('Cluster_data.csv', 'a') as file1:
        csv_writer = csv.writer(file1)
        csv_writer.writerow(centroid_set[j-15])
   # print(labels)

    colors = ["y.", "r.", "g.", "b.", "m.", "k."]
# #############################################################################
# Plot result
    for i in range(len(X)):
       #print ("coordinate:" , X[i], "label:", labels[i])
       plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

    plt.scatter(centroid[:, 0],centroid[:, 1], marker="x", s=150, linewidths=5, zorder=10)
    plt.savefig('C:\\Users\\shubh\\PycharmProjects\\User_engagement\\cluster_plot\\cluster_6_' + str(j) + ".png")

    plt.title('6 Means Clustering (Users: %d)' % labels.size)
    plt.show()
    plt.clf()
for i in range(15, 40):
    #print centroid_set[i-15]
    for j in range(0, 6):
        plt.plot(centroid_set[i-15][j][0], centroid_set[i-15][j][1], colors[j], markersize=10)
plt.savefig('centroid.png')
plt.title('Centroid Plot')
plt.show()