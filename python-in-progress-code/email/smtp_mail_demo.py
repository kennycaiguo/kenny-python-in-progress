import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_email = "kennycai8888@yahoo.com"
pwd = "Guohua1975cai"    # 这个密码就会你雅虎邮箱的密码

to_email = "kennycai8888@outlook.com@qq.com"
smtp_server = "smtp.mail.yahoo.com"     # 使用雅虎的smtp服务

# 发送文本邮件 和 html邮件
# msg = MIMEText('hello, This a test email by python','plain', 'utf-8')
msg = MIMEText("<html><body><h2 align='center'>RONG YES!</h2></body></html>", 'html', 'utf-8')
msg['From'] = _format_addr("rong <{}>".format(from_email))      # 发件人
msg['To'] = _format_addr('小白 <{}>'.format(to_email))        # 收件人
msg['Subject'] = Header('测试主题', 'utf-8').encode()       # 主题

server = smtplib.SMTP(smtp_server, 587)
# server.ehlo()  # 向雅虎发送SMTP 'ehlo' 命令
server.starttls()   # 加密SMTP
# server.set_debuglevel(1)          # debug查看状态
server.login(from_email, pwd)
server.sendmail(from_email, [to_email], msg.as_string())
server.quit()


