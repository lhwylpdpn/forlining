#coding:utf-8
import pymysql
import os


def  clac_json():
	avg_num=[]
	conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='stock_foreign',port=3306)
	cur_stock=conn.cursor()
	sql="SELECT AVG(b) FROM (SELECT STR_TO_DATE(order_time_send,'%Y-%c-%d') AS a,COUNT(*) AS b FROM `order` GROUP BY STR_TO_DATE(order_time_send,'%Y-%c-%d') HAVING a>DATE_ADD(NOW(),INTERVAL -7 DAY)) a"
	cur_stock.execute(sql)
	res=cur_stock.fetchall()
	for r in res:
		word1=str(float(r[0]))

	sql="SELECT SUM(CASE WHEN  lots_A=0.01 THEN 1 END )/COUNT(*) FROM `order_result` "
	cur_stock.execute(sql)
	res=cur_stock.fetchall()
	for r in res:
		word2=str(float(r[0]))
	
	cur_stock.close()
	conn.close()

	word='{"avg_profit":0.02,"avg_profit_week":0.1,"success":'+word2+',"success_profit":0.3,"max_margin":0.23,"max_huiche":0.25,"avg_num":'+word1+'}'
	create_json(word)
def  create_json(word):
	file_object = open('json/static.json','w')
	file_object.write(word+"\n")
	file_object.close()
if __name__ == "__main__":

	#clac_json()
	while(1):
		if(os.path.exists("C:/Program Files (x86)/MetaTrader 4/MQL4/Files/testtttttttt.json")):
			print("3")
			os.remove("C:/Program Files (x86)/MetaTrader 4/MQL4/Files/testtttttttt.json")