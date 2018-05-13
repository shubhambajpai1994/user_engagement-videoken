import os
import csv
def extract_user_id():
    for user in os.listdir("C:/Users/shubh/PycharmProjects/User_Engagement/user_file/"):
        usr = user.split(".json")[0]
        with open('user_id.csv', 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([usr])

extract_user_id()