import json
import csv
import os


def user_count():
    users = []
    for file in os.listdir("C:/Users/shubh/PycharmProjects/User_Engagement/logdumps_organisationX/"):
        print file
        with open("C:/Users/shubh/PycharmProjects/User_Engagement/logdumps_organisationX/" + file) as json_data:
            x = json.load(json_data)

        for feature in x:
            if feature['uid'] not in users:
                users.append(feature['uid'])
                with open('users1.csv', 'a') as dataFile:
                    csv_writer = csv.writer(dataFile)
                    csv_writer.writerow([feature['uid'],feature['email_id']])
    print len(users)
    return users

user_count()
