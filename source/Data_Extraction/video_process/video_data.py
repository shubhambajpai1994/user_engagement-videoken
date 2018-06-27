import json
import re
import os
import datetime
import matplotlib.pyplot as plt

def user_video_data():
    # videos_played= [[]]
    with open(
            "/Users/shubham.bajpai/Documents/User_Engagement/source/Data_Extraction/video_process/user_id_daywise_timespent.json") as json_data:
        x = json.load(json_data)
        user_data = {}
        max_videos = {}
        max_time = {}
        for i in range(15, 40):
            max_videos[i] = 1.0
            max_time[i] = 1.0
        for feature in x:
            video = {}
            for i in range(15, 40):
                video[i] = [0, 0]
            for days in x[feature].keys():
                year = days[:4]
                month = days[5:7]
                day = days[8:]
                # print year
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
                            # print time, videos
                        if max_videos[week_number] < videos:
                            max_videos[week_number] = videos
                        if max_time[week_number] < time:
                            max_time[week_number] = time
                    video[week_number] = [videos, time]
            user_data[feature] = video
        Z1 = sorted(user_data.keys())
        sorted_videos = []
        for index in Z1:
            sorted_videos.append(user_data[index])
            # print index,user_data[index]
    for users in Z1:
        key = user_data[users].keys()
        # print user_data[users]
        # print key
        value = []
        for i in range(15, 40):
            if i in range(15, 38):
                value.append(user_data[users][i][0])
            else:
                value.append(0)
        plt.plot(key, value)
        # plt.show()
        #plt.savefig("/Users/shubham.bajpai/Documents/User_Engagement/video_watched_plot/" + users + ".png")
        plt.clf()
    for users in Z1:
        key = user_data[users].keys()
        # print user_data[users]
        # print key
        value = []
        for i in range(15, 40):
            if i in range(15, 38):
                value.append(user_data[users][i][1])
            else:
                value.append(0)
        plt.plot(key, value)
        # plt.show()
        #plt.savefig("/Users/shubham.bajpai/Documents/User_Engagement/video_time_plot/" + users + ".png")
        plt.clf()
    for users in Z1:
        key=user_data[users].keys()
        #print user_data[users]
        #print key
        value = []
        for i in range(15, 40):
            if i in range(15,38):
                value.append(user_data[users][i][0])
            else:
                value.append(0)
        plt.plot(key, value)
    plt.savefig('video_watched.png')
    plt.show()
    plt.clf()
    #plt.clf()
    for users in Z1:
        key=user_data[users].keys()
        #print user_data[users]
        #print key
        value = []
        for i in range(15, 40):
            if i in range(15,38):
                value.append(user_data[users][i][1])
            else:
                value.append(0)
        plt.plot(key, value)
    plt.savefig('video_time_plot.png')
    plt.show()
    plt.clf()


user_video_data()