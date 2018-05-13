import json
import csv
import os
import datetime
import matplotlib.pyplot as plt


def extract_discussion():
    print "discussion"
    user_wise_data = {}
    global max_week
    max_week = 0.0
    for file in os.listdir("C:/Users/shubh/PycharmProjects/User_Engagement/user_file/"):
            discussion_clicks = {}
            for i in range(15, 40):
                discussion_clicks[i]=0.0
            with open("C:/Users/shubh/PycharmProjects/User_Engagement/user_file/" + file, 'r') as df:
                for l in df.readlines():
                    d = json.loads(l)
                    if d['user_action'] and "Discussions" in d['user_action']:

                        #extract week number based on iso gregorian calendar

                        year = d['date'][:4]
                        month = d['date'][5:7]
                        day = d['date'][8:]
                        dt = datetime.date(int(year), int(month), int(day))
                        week_number = dt.isocalendar()[1]
                        if week_number in discussion_clicks:
                            discussion_clicks[week_number] += 1.0
                        else:
                            discussion_clicks[week_number] = 1.0
                for week in range(15,40):
                    if discussion_clicks[week]>max_week:
                        max_week=discussion_clicks[week]
                user_wise_data[file] = discussion_clicks
    return user_wise_data


def save_discussion_data():
    discussion_clicks = extract_discussion()
    for users in discussion_clicks:
        for week in range(15,40):
            discussion_clicks[users][week]=discussion_clicks[users][week]/max_week
    for user in discussion_clicks:
        #print user.split(".json")[0]
        usr = user.split(".json")[0]
        index = discussion_clicks[user].keys()
        count = discussion_clicks[user].values()
        #print index
        #print count
        with open('discussion_user_data1.csv', 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(count)
        plt.plot(index, count)
        #plt.show()
        plt.savefig("C:/Users/shubh/PycharmProjects/User_Engagement/discussion_plot1/"+usr+".png")
        plt.clf()
    for user in discussion_clicks:
        index = discussion_clicks[user].keys()
        count = discussion_clicks[user].values()
        plt.plot(index, count)
    plt.savefig("C:/Users/shubh/PycharmProjects/User_Engagement/source/Data_Extraction/discussion/discussion_plot1.png");
    plt.show();

save_discussion_data()
