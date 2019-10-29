from __future__ import absolute_import
import smtplib
from email.mime.text import MIMEText
from Qshop.settings import MAIL_PASSWORD,MAIL_PORT,MAIL_SENDER,MAIL_SERVER

from Qshop.celery import app

@app.task
def sendMil(content,email):
    content = """
            点击链接进行修改密码
            <a href="%s">点击确认</a>
        """ % (content)
    print(content)

    message = MIMEText(content, 'html', 'utf-8')
    message["To"] = email
    message['From'] = MAIL_SENDER
    message['Subject'] = '密码修改'
    try:
        smtp = smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT)
        smtp.login(MAIL_SENDER, MAIL_PASSWORD)
        smtp.sendmail(MAIL_SENDER, [email], message.as_string())
        smtp.close()
    except Exception as e:
        return str(e)
    else:
        return