# coding : utf-8
# author : adair

import xlsxwriter
import sys,time,datetime
reload(sys)
sys.setdefaultencoding("utf-8")


d1 = datetime.datetime.now()
d3 = d1 + datetime.timedelta(days = -1)
yestoday= datetime.date.today() + datetime.timedelta(days=-1)
#print 'sales_'+yestoday.strftime('%Y-%m-%d') +'.xlsx'

workbook   = xlsxwriter.Workbook('sales_'+yestoday.strftime('%Y-%m-%d') +'.xlsx')   # 创建名为filename.xlsx的.xlsx文件，注意，这个库每次打开的文件都会被清空内容
worksheet1 = workbook.add_worksheet()               # 创建worksheet，括号里可传worksheet的名字，如workbook.add_worksheet('abc')

format=workbook.add_format()
format.set_border(1)

format_title=workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#ffcc99')
format_title.set_align('center')
format_title.set_bold()



# 给出内容标题  
headings = [u'日期',u'类目一', u'类目二', u'类目三',u'官网',u'天猫',u'1mall',u'京东']    

ldate=[]
lcat1=[]
lcat2=[]
lcat3=[]
lgw=[]
ltmall=[]
lymall=[]
ljd=[]

f =file( "/home/hongdai.zou/crontab/sales.tmp", "r" )
for lines in f.readlines():
    #print len(lines)
    line=lines.strip().split("\t")
    #print line
    date=line[0]
    cat1=line[1]
    cat2=line[2]
    cat3=line[3]
    gw=line[4]
    tmall=line[5]
    ymall=line[6]
    jd=line[7]
    
    ldate.append(date)  
    lcat1.append(cat1)
    lcat2.append(cat2) 
    lcat3.append(cat3)
    lgw.append(round(float(gw)))
    ltmall.append(round(float(tmall)))
    lymall.append(round(float(ymall)))
    ljd.append(round(float(jd)))     
    

#print ljd

worksheet1.write_row('A1', headings,format_title)   # 从$A$1位置开始横向把内容标题写入
worksheet1.write_column('A2', ldate,format)
worksheet1.write_column('B2', lcat1,format)
worksheet1.write_column('C2', lcat2,format)
worksheet1.write_column('D2', lcat3,format)
worksheet1.write_column('E2', lgw,format)
worksheet1.write_column('F2', ltmall,format)
worksheet1.write_column('G2', lymall,format)
worksheet1.write_column('H2', ljd,format)

workbook.close()
