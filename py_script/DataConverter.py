import os;
import sys;

#logfileName = sys.argv[1]
logfileName = "2_3_src.csv"

src_file = open(logfileName, "r")
result_file = open("result.csv","w")

lines = src_file.readlines()

for line in lines:
    tokens = line.split(";")
    #line_result = "DTM] LANE:0" + '{:02}'.format(int(tokens[0]) + tokens[1][1:-1]
    #line_result = line_result + "SPEED:" + '{:.2}'.format(float(tokens[2])) + "OCC1:000 OCC2:000 LENGTH:000"
    #result_file.write(line_result)


result_file.close()
src_file.close()

                                                 
                                                
