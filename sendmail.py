#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
发送html文本邮件
'''
import sys
#filestr = '/usr/local/shell/wd.html'          
filestr = sys.argv[1]
sname= sys.argv[2]
content=  sys.argv[3]
print filestr
#content =  file(filestr).read()
#邮件正文
#content = "test youh"

import smtplib  
import datetime
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email.MIMEBase import MIMEBase
from email import Encoders

today = datetime.date.today()
deltadays = datetime.timedelta(days=8)
yesterday = today -deltadays
ISOFORMAT='%Y%m%d'


print today
print deltadays
print yesterday


#mailto_list=["aaa@xxx.com"] 
mailto_list=["aaa@xxx.com","nemo@xxx.com"] 
mail_host="smtp.gmail.com"  #设置服务器
mail_user=""    #用户名
mail_pass=""   #口令 
mail_postfix="xxx.com"  #发件箱的后缀

#创建一个带附件的实例
msg = MIMEMultipart()


me="aaa@xxx.com"   #这里的hello可以任意设置，收到信后，将按照设置显示
body = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
#构造附件1
msg.attach(body)
msg['Subject'] = sname   #设置主题
msg['From'] = me
msg['To'] = ",".join(mailto_list)
#附件内容，若有多个附件，就添加多个part, 如part1，part2，part3
part = MIMEBase('application', 'octet-stream')
# 读入文件内容并格式化，此处文件为当前目录下，也可指定目录 例如：open(r'/tmp/123.txt','rb')
part.set_payload(open(filestr,'rb').read())
Encoders.encode_base64(part)
## 设置附件头
part.add_header('Content-Disposition', 'attachment; filename='+filestr+'')
msg.attach(part)


def send_mail(mailto_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容


    try:
	s = smtplib.SMTP_SSL(mail_host,465)  #使用SSL 465端口登陆
	#s = smtplib.SMTP()      #默认使用25端口登陆	
        #s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, mailto_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,"前一天报警统计",content):  
        print "发送成功"  
    else:  
        print "发送失败"

