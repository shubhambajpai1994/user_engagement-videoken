import numpy as np
import matplotlib.pyplot as plt
import json
#from matplotlib import style
import csv
import datetime
#style.use("ggplot")

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
        change_data[i][0] = change_data[i][0]*2
    video_values.append(change_data)
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
        #val2 = val1+val2
        #print val1, val2
        #val1 = video[user][1]+video[user][2]
        week_data[i].append([val1, val2])
centroid_set = []
for j in range(0, 25):
    centroid_set.append([])

video_week_data = []
for i in range(0, 25):
    video_week_data.append([])
for user in range(0, count):
    for i in range(0, 25):
        video_week_data[i].append([video_values[user][i + 15][0], video_values[user][i + 15][1]])
       # print video_week_data[i]
for j in range(15, 40):
        #X = np.array(week_data[j-15])
        #print X
        X = np.array(video_week_data[j-15])
        #print X
        kmeans = KMeans(n_clusters=2)
        kmeans.fit(X)
        centroid = kmeans.cluster_centers_
        labels = kmeans.labels_
        video_val = []
        non_video_val = []
        count_nv = []
        count_v = []
        for index in range(0, 2):
            video_val.append(0.0)
            count_v.append(0.0)
        for index in range(0, 3):
            non_video_val.append(0.0)
            count_nv.append(0.0)
        #print labels
        set1 = []
        set2 = []
        setv1 = []
        setv2 = []
        for user in range(0, count):
            #print labels[user]
            if labels[user] == 0:
                set1.append(week_data[j-15][user])
                setv1.append(video_week_data[j-15][user])
                video_val[0]=video_val[0]+((float)(video_week_data[j-15][user])*100.0)
                count_v[0]+=1.0
                #print set1
            else:
                set2.append(week_data[j-15][user])
                setv2.append(video_week_data[j-15][user])
                video_val[1] = video_val[1] + ((float)(video_week_data[j - 15][user]) * 100.0)
                count_v[1]+=1.0
        #print float(video_week_data[15][user][0]+video_week_data[15][user][1])
        for index in range(0, 2):
            if count[index] != 0.0:
                video_val[index] = (video_val[index]) / count[index]
        with open('mean_video_hierarchial_with_constraint_clustering.csv', 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(video_val)
        X = np.array(set1)
       # print X
        Y = np.array(set2)
        #print Y
        labels1=[]
        labels2=[]
        if X.size>3:
            kmeans = KMeans(n_clusters=3)
            kmeans.fit(X)

            centroid1 = kmeans.cluster_centers_
            labels1 = kmeans.labels_
        elif X.size>0:
            kmeans = KMeans(n_clusters=X.size-1)
            kmeans.fit(X)

            centroid1 = kmeans.cluster_centers_
            labels1 = kmeans.labels_
        if Y.size>3:
            kmeans = KMeans(n_clusters=3)
            kmeans.fit(Y)
            centroid2 = kmeans.cluster_centers_
            labels2 = kmeans.labels_
        elif Y.size>0:
            kmeans = KMeans(n_clusters=Y.size-1)
            kmeans.fit(Y)

            centroid2 = kmeans.cluster_centers_
            labels2 = kmeans.labels_
        #print (centroid)
       # print(labels)

        colors = ["y.", "r.", "g."]
        colors1 = ["b.", "m.", "k."]
        if X.size>0:
            for i in range(len(X)):
               #print ("coordinate:" , X[i], "label:", labels[i])
               val1=float(setv1[i][0])+float(setv1[i][1])
               val2= float(X[i][0])+float(X[i][1])
               plt.plot(val1, val2, colors[labels1[i]], markersize=10)
        if Y.size>0:
            for i in range(len(Y)):
               #print ("coordinate:" , X[i], "label:", labels[i])
               val1 = float(setv2[i][0]) + float(setv2[i][1])
               val2 = float(Y[i][0]) + float(Y[i][1])
               plt.plot(val1, val2, colors1[labels2[i]], markersize=10)
        if X.size>0:
            plt.scatter(centroid1[:, 0], centroid1[:, 1], marker="x", s=150, linewidths=5, zorder=10)
        if Y.size>0:
            plt.scatter(centroid2[:, 0], centroid2[:, 1], marker="x", s=150, linewidths=5, zorder=10)
        #plt.savefig("C:\Users\shubh\PycharmProjects\User_engagement\multi_level_cluster_plot\cluster_6_"+str(j)+".png")
        plt.title('Multi-Level Clustering (Users: %d)' % labels.size)
        plt.show()
        plt.clf()
        l1=0
        l2=0
        l3=0
        l4=0
        l5=0
        l6=0
        for i in labels1:
            if i==0:
                l1+=1
            elif i==1:
                l2+=1
            else:
                l3+=1
        for i in labels2:
            if i==0:
                l4+=1
            elif i==1:
                l5+=1
            else:
                l6+=1
        print l1,l2,l3,l4,l5,l6