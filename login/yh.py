# 'FDDXEOUKIGGAZGTH'


import smtplib
import time
from email.mime.text import MIMEText
from random import randint


def _gettime():
    timelist = str(time.asctime()).split(' ')
    dict1 = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    month = dict1[timelist[1]]  # month
    day = timelist[2]  # day
    year = timelist[4]  # year
    hms = timelist[3]
    return f"{month}/{day}/{year} {hms}"


recode = randint(1000000, 9999999)
message = MIMEText(f"""
{' ' * 10}您的密码正在被重置,验证码为{recode}.
{' ' * 10}请将验证码填写在主窗口内以完成验证.
{' ' * 10}请勿将验证码透露给任何人!!!
{' ' * 10}如果不是您本人或本人允许的操作,请忽略此消息.
{' ' * 10}本邮件为脚本自动发送,请勿回复

{' ' * 30}pylogin,
{' ' * 30}{_gettime()}

""", 'plain', 'utf-8')
message['Subject'] = '[pylogin] Reset your password'
message['From'] = 'daicx135246@163.com'
message['To'] = '3439077245@qq.com'


def _send(smsg=message):
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect('smtp.163.com')  # host
        smtpObj.login('daicx135246@163.com', 'FDDXEOUKIGGAZGTH')  # user,pwd
        smtpObj.sendmail(
            'daicx135246@163.com', ['3439077245@qq.com', 'daicx135246@163.com'],
            smsg.as_string())  # uesr,receivers[],string
        smtpObj.quit()
        return True
    except smtplib.SMTPException as e:
        return False


def reset():
    usermail = input('please input your reg mail')
    pass


_send()
