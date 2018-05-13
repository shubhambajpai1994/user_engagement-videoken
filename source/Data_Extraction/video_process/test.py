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
    plt.savefig("C:/Users/shubh/PycharmProjects/User_Engagement/video_watched_plot/" + users + ".png")
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
    plt.savefig("C:/Users/shubh/PycharmProjects/User_Engagement/video_time_plot/" + users + ".png")
    plt.clf()