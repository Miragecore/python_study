import psycopg2

conn = psycopg2.connect("dbname=SmartVDS user=meta password=meta3327")

cur = conn.cursor()


strQuery = "SELECT tregionid, datetime, speed FROM tb_traffic_info"
strQuery += " WHERE datetime BETWEEN '2016-02-03 09:19:23' AND '2016-02-03 12:00:00' AND tregionid BETWEEN '1' AND '4'"       

cur.execute(strQuery)

items  = cur.fetchall()

print items[0][1].strftime("%H.%M.%S")
       
