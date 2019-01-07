import requests as req

name = "Mio"
uid = "UCp-5t9SrOQwXMU7iIjQfARg"
url = "https://socialblade.com/youtube/channel/"+uid+"/monthly"
r = req.get(url)
print(r.status_code)

DailySubscribers = r.text.split("DailySubscribers\'),\r\n\t// CSV or path to a CSV file.\r\n\t")[1].split(", {\r\n\t\t\ttitle:")[0]
DailySubscribers = DailySubscribers.replace("\"","")
DailySubscribers = DailySubscribers.replace("\\n","")
DailySubscribers = DailySubscribers.replace(" + ","\n")

TotalSubscribers = r.text.split("TotalSubscribers\'),\r\n\t// CSV or path to a CSV file.\r\n\t")[1].split(", {\r\n\t\t\ttitle:")[0]
TotalSubscribers = TotalSubscribers.replace("\"","")
TotalSubscribers = TotalSubscribers.replace("\\n","")
TotalSubscribers = TotalSubscribers.replace(" + ","\n")

DailyVideoViews = r.text.split("DailyVideoViews\'),\r\n\t// CSV or path to a CSV file.\r\n\t")[1].split(", {\r\n\t\t\ttitle:")[0]
DailyVideoViews = DailyVideoViews.replace("\"","")
DailyVideoViews = DailyVideoViews.replace("\\n","")
DailyVideoViews = DailyVideoViews.replace(" + ","\n")

TotalVideoViews = r.text.split("TotalVideoViews\'),\r\n\t// CSV or path to a CSV file.\r\n\t")[1].split(", {\r\n\t\t\ttitle:")[0]
TotalVideoViews = TotalVideoViews.replace("\"","")
TotalVideoViews = TotalVideoViews.replace("\\n","")
TotalVideoViews = TotalVideoViews.replace(" + ","\n")

fileObject = open(name + '_' + 'DailySubscribers' + '.CSV', 'w')
fileObject.write(DailySubscribers)
fileObject.close()

fileObject = open(name + '_' + 'TotalSubscribers' + '.CSV', 'w')
fileObject.write(TotalSubscribers)
fileObject.close()

fileObject = open(name + '_' + 'DailyVideoViews' + '.CSV', 'w')
fileObject.write(DailyVideoViews)
fileObject.close()

fileObject = open(name + '_' + 'TotalVideoViews' + '.CSV', 'w')
fileObject.write(TotalVideoViews)
fileObject.close()