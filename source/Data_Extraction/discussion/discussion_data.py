import json
import csv
import os
import datetime
import matplotlib.pyplot as plt


def extract_discussion():
    print "discussion"
    user_wise_data = {}
    for file in os.listdir("/Users/shubham.bajpai/Documents/User_Engagement/user_file/"):
            discussion_clicks = {}
            for i in range(15, 40):
                discussion_clicks[i]=0
            with open("/Users/shubham.bajpai/Documents/User_Engagement/user_file/" + file, 'r') as df:
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
                            discussion_clicks[week_number] += 1
                        else:
                            discussion_clicks[week_number] = 1

                user_wise_data[file] = discussion_clicks
    return user_wise_data


def save_discussion_data():
    discussion_clicks = extract_discussion()

    for user in discussion_clicks:
        #print user.split(".json")[0]
        usr = user.split(".json")[0]
        index = discussion_clicks[user].keys()
        count = discussion_clicks[user].values()
        #print index
        #print count
        with open('discussion_user_data.csv', 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(count)
        plt.plot(index, count)
        #plt.show()
        plt.savefig("/Users/shubham.bajpai/Documents/User_Engagement/discussion_plot/"+usr+".png")
        plt.clf()
    for user in discussion_clicks:
        index = discussion_clicks[user].keys()
        count = discussion_clicks[user].values()
        plt.plot(index, count)
    plt.savefig("/Users/shubham.bajpai/Documents/User_Engagement/source/Data_Extraction/discussion/discussion_plot.png");
    plt.show();

save_discussion_data()
