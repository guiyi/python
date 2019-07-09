# coding : utf-8
# author : adair
# date: 2019-07-09

#1. Opencart 日志设置
'''
//Adair 日志记录user_id start//
$obj = json_encode($session);
$b = json_decode($obj);

$customer_id = '';
if(isset($b->data->customer_id)){
    $customer_id = $b->data->customer_id;

}
setcookie('at_uvid', $customer_id, ini_get('session.cookie_lifetime'), ini_get('session.cookie_path'), ini_get('session.cookie_domain'));
//Adair 日志记录user_id end //


nginx.conf

http {
#分隔符替换为^^A
log_format  main  '$uid^^A$remote_addr^^A$remote_user^^A[$time_local]^^A$request^^A'
                  '$status^^A$body_bytes_sent^^A$http_referer^^A'
                  '$http_user_agent^^A$http_x_forwarded_for';
#access_log  /usr/local/var/logs/access.log ;
}


servers/6_dfrobot

server {

# 在server块添加以下代码
# 设置默认值
 set $uid "-";

# 存在值则赋值
if ( $http_cookie ~* "at_uvid=(\S+)(;.*|$)"){
      set $uid $1;
 }

access_log  /usr/local/var/logs/nginx/6dfrobot.access.log  main;

}
'''

#2. 日志表
'''CREATE TABLE `df_log` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `ip` varchar(20) DEFAULT NULL,
  `remote_user` varchar(20) DEFAULT NULL,
  `time_local` varchar(100) DEFAULT NULL,
  `request_method` varchar(10) DEFAULT NULL,
  `http_request` varchar(200) DEFAULT NULL,
  `request_server` varchar(20) DEFAULT NULL,
  `status` int(5) DEFAULT NULL,
  `body_bytes_sent` int(11) DEFAULT NULL,
  `http_referer` varchar(300) DEFAULT NULL,
  `http_user_agent` varchar(500) DEFAULT NULL,
  `http_x_forwarded_for` varchar(300) DEFAULT NULL,
  `date_added` datetime DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8'''

#3. 将日志清洗后插入日志表

import pymysql
import time

#数据库连接
def connDB():
    global conn,sql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='****', db='****', charset='utf8')
    cur = conn.cursor()

path ='/usr/local/var/logs/nginx/'
file = '6dfrobot.access.log'
filePath = path+file

with open(filePath,encoding='utf-8')as f:
    #print(f.readlines()) #将文件内容读取到列表中
    for i in f.readlines():
        logInfo = i.split("^^A")
        #print(logInfo[0],logInfo[1],logInfo[2],logInfo[3],logInfo[4],logInfo[5],logInfo[6],logInfo[7],logInfo[8],logInfo[9])
        
        customer_id = logInfo[0]
        ip = logInfo[1]
        remote_user = logInfo[2]
        time_local = logInfo[3]
        requestInfo = logInfo[4].split(" ")
        request_method = requestInfo[0]
        http_request = requestInfo[1]
        request_server= requestInfo[2]
        status = logInfo[5]
        body_bytes_sent = logInfo[6]
        http_referer = logInfo[7]
        http_user_agent = logInfo[8]
        http_x_forwarded_for = logInfo[9]
        

        connDB()
        date_added =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
        sql="INSERT IGNORE INTO `df_log` (`customer_id`,`ip`,`remote_user`,`time_local`,`request_method`,`http_request`,`request_server`,`status`,`body_bytes_sent`,`http_referer`,`http_user_agent`,`http_x_forwarded_for`,`date_added`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            with conn.cursor() as cursor:
                #print(customer_id,ip,remote_user,time_local,request_method,http_request,request_server,status,body_bytes_sent,http_referer,http_user_agent,http_x_forwarded_for)
                cursor.execute(sql,(customer_id,ip,remote_user,time_local,request_method,http_request,request_server,status,body_bytes_sent,http_referer,http_user_agent,http_x_forwarded_for,date_added))
                conn.commit()
                cursor.close()
        finally:
            pass



