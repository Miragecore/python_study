import VDS_Object
import datetime

def ReadLog(fileName):

	f = open(fileName,"r")

	lines = f.readlines()

	time = datetime.datetime(2016, 1, 1, 1, 1, 1, 1)

	detectObjList = [];

	#datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S.%f")
	seqNo = 0

	for line in lines:
		if line[0] == "[":
			tokens = line.split(" ")			
			time = datetime.datetime.strptime(tokens[0], "[%H:%M:%S.%f]")
			seqNo += 1
		else :
			tokens = line.split(",")
			dObj = VDS_Object.DetectObject(time,int(tokens[1]),
				                               float(tokens[3]),
				                               float(tokens[5]),
				                               float(tokens[7]),
				                               float(tokens[9]),
				                               float(tokens[11]))
			dObj.seqNo = seqNo

			detectObjList.append(dObj)
	f.close()

	return detectObjList;