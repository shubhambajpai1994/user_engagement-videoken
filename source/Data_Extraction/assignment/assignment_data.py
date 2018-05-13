import json
import csv
import os
import datetime
import matplotlib.pyplot as plt


def extract_Assignment():
    print "Assignments"
    user_wise_data = {}
    for file in os.listdir("C:/Users/shubh/PycharmProjects/User_Engagement/user_file/"):
            Assignment_clicks = {}
            for i in range(15, 40):
                Assignment_clicks[i]=0
            with open("C:/Users/shubh/PycharmProjects/User_Engagement/user_file/" + file, 'r') as df:
                for l in df.readlines():
                    d = json.loads(l)
                    if d['user_action'] and "Assignments" in d['user_action']:

                        #extract week number based on iso gregorian calendar

                        year = d['date'][:4]
                        month = d['date'][5:7]
                        day = d['date'][8:]
                        dt = datetime.date(int(year), int(month), int(day))
                        week_number = dt.isocalendar()[1]
                        if week_number in Assignment_clicks:
                            Assignment_clicks[week_number] += 1
                        else:
                            Assignment_clicks[week_number] = 1

                user_wise_data[file] = Assignment_clicks
    return user_wise_data


def save_Assignment_data():
    Assignment_clicks = extract_Assignment()

    for user in Assignment_clicks:
        #print user.split(".json")[0]
        usr = user.split(".json")[0]
        index = Assignment_clicks[user].keys()
        count = Assignment_clicks[user].values()
        #print index
        #print count
        with open('Assignment_user_data.csv', 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(count)
        plt.plot(index, count)
        #plt.show()
        plt.savefig("C:/Users/shubh/PycharmProjects/User_Engagement/Assignment_plot/"+usr+".png")
        plt.clf()
    for user in Assignment_clicks:
        index = Assignment_clicks[user].keys()
        count = Assignment_clicks[user].values()
        plt.plot(index, count)
    plt.savefig("C:/Users/shubh/PycharmProjects/User_Engagement/source/Data_Extraction/assignment/Assignment_plot.png");
    plt.show();

save_Assignment_data()
