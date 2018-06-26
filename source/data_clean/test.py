import json

with open('logdump_100000.json') as json_data:
	data = json.load(json_data)
	for r in data:
		fo = open("C:\\Users\shubh\\Desktop\\Project Elective\\files\\"+r['uid']+".txt","a")
		fo.write(r['timestamp']+"    "+r['client_msg']+"\n")
		fo.close 
	print("finish")

