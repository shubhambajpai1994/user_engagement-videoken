import json
import csv
import os
import datetime
import matplotlib.pyplot as plt


def extract_mmtoc():
    print "mmtoc"
    user_wise_data = {}
    for file in os.listdir("C:/Users/shubh/PycharmProjects/User_Engagement/user_file/"):
            mmtoc_clicks = {}
            for i in range(15, 40):
                mmtoc_clicks[i]=0.0
            with open("C:/Users/shubh/PycharmProjects/User_Engagement/user_file/" + file, 'r') as df:
                for l in df.readlines():
                    d = json.loads(l)
                    if d['user_action'] and "mmtoc" in d['user_action']:

                        #extract week number based on iso gregorian calendar

                        year = d['date'][:4]
                        month = d['date'][5:7]
                        day = d['date'][8:]
                        dt = datetime.date(int(year), int(month), int(day))
                        week_number = dt.isocalendar()[1]
                        if week_number in mmtoc_clicks:
                            mmtoc_clicks[week_number] += 1.0
                        else:
                            mmtoc_clicks[week_number] = 1.0

                user_wise_data[file] = mmtoc_clicks
    return user_wise_data


def save_mmtoc_data():
    mmtoc_clicks = extract_mmtoc()

    for user in mmtoc_clicks:
        #print user.split(".json")[0]
        usr = user.split(".json")[0]
        index = mmtoc_clicks[user].keys()
        count = mmtoc_clicks[user].values()
        #print index
        #print count
        with open('mmtoc_user_data.csv', 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(count)
        plt.plot(index, count)
        #plt.show()
        plt.savefig("C:/Users/shubh/PycharmProjects/User_Engagement/mmtoc_plot/"+usr+".png")
        plt.clf()
    for user in mmtoc_clicks:
        index = mmtoc_clicks[user].keys()
        count = mmtoc_clicks[user].values()
        plt.plot(index, count)
    plt.savefig("C:/Users/shubh/PycharmProjects/User_Engagement/source/Data_Extraction/mmtoc/mmtoc_plot.png");
    plt.show();

save_mmtoc_data()
