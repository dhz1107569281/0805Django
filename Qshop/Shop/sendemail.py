import smtplib
from email.mime.text import MIMEText

content="""邮件试水!!!"""

sender='1107569281@qq.com'

recver="""1107569281@qq.com,
1497259593@qq.com,
1165177422@qq.com"""

password="aaptspxekxeqfhhd"

message=MIMEText(content,"plain","utf-8")
message["To"]=recver
message["From"]=sender
message["Subject"]="???"

smtp=smtplib.SMTP_SSL("smtp.qq.com",465)
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(",\n"),message.as_string())
smtp.close()