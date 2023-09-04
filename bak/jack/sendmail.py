#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime
import time

my_sender = '1062097940@qq.com'  # 发件人邮箱账号
my_pass = 'hnrssnkmuudnbdci'  # 发件人邮箱密码
# my_user = 'yu_zhelei@163.com'  # 收件人邮箱账号(这里发自己)
# my_user = '423595855@qq.com'  # 收件人邮箱账号(这里发自己)
user_arr = ['yu_zhelei@163.com', '423595855@qq.com']


def mail(message):
    ret = True
    try:
        for send_to in user_arr:
            current_dt = time.strftime("%Y-%m-%d", time.localtime())
            # current_dt = datetime.strptime(current_dt, '%Y-%m-%d')
            title = current_dt.split(" ")[0] + "投资操作"
            msg = MIMEText(message, 'plain', 'utf-8')
            msg['From'] = formataddr(["Frankie888", my_sender])  # 发件人昵称
            msg['To'] = formataddr(["李狗泽", send_to])  # 接收人昵称
            msg['Subject'] = title  # 邮件的主题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            server.login(my_sender, my_pass)  # 发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [send_to, ], msg.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret = False
        ret = False
        print(e)
    return ret


if __name__ == "__main__":
    ret = mail("Test")
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
