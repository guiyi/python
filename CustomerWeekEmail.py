# coding : utf-8
# author : adair
# date: 2018-01-22

import pymysql
import datetime,time,re
import xlsxwriter

DateTime =time.strftime("%Y-%m-%d", time.localtime());
OutFile  = open("Customer_"+DateTime+".txt","a",encoding='utf-8')

#数据库连接
def connLinajia():
    global conn,sql
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='***', db='***', charset='utf8')
    cur = conn.cursor()  
 

def getCustomerWeekData():
	today  = datetime.datetime.now()

	last_week_start = today - datetime.timedelta(days=7)
	last_week_start = last_week_start.strftime('%Y-%m-%d')

	last_week_end = today - datetime.timedelta(days=1)
	last_week_end = last_week_end.strftime('%Y-%m-%d')

	connLinajia() 
	sql="select email,firstname,lastname from customer where date_added>="+"'"+last_week_start+"'"+" and date_added<="+"'"+last_week_end+"'"+""
	try:
		with conn.cursor() as cursor:
			#print(sql)
			cursor.execute(sql)
			rst = cursor.fetchall()
			rst_list = list(rst)


			workbook   = xlsxwriter.Workbook('newCustomer_'+last_week_start +'&'+last_week_end+'.xlsx')   # 创建名为filename.xlsx的.xlsx文件，注意，这个库每次打开的文件都会被清空内容
			worksheet1 = workbook.add_worksheet()               # 创建worksheet，括号里可传worksheet的名字，如workbook.add_worksheet('abc')

			format=workbook.add_format()
			format.set_border(1)

			format_title=workbook.add_format()
			format_title.set_border(1)
			format_title.set_bg_color('#e67300')
			format_title.set_align('center')
			format_title.set_bold()
			worksheet1.set_column('A:C', 30)



			# 给出内容标题  
			headings = [u'Email',u'Firstname', u'Lastname']    

			lemail=[]
			lfirstname=[]
			llastname=[]
			for row in rst_list:
				#print(list(row))
				email = list(row)[0]
				firstname = list(row)[1]
				lastname = list(row)[2]

				lemail.append(email) 
				lfirstname.append(firstname)
				llastname.append(lastname)
				#print(lemail) 
				#print(lastname)
				worksheet1.write_row('A1', headings,format_title)   # 从$A$1位置开始横向把内容标题写入
				worksheet1.write_column('A2', lemail,format)
				worksheet1.write_column('B2', lfirstname,format)
				worksheet1.write_column('C2', llastname,format)
      
			workbook.close() 

	finally:
		pass
	#关闭指针对象
	cursor.close()
	#关闭连接对象   
	conn.close()  




#入口函数
if __name__ == '__main__':
	getCustomerWeekData()
   
