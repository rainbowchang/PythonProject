# 发邮件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
# 输入SMTP服务器地址:
smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# 输入收件人地址:
to_addr = input('请输入收件人邮箱地址To: ')

msg = MIMEText('hi,Python邮件发送测试', 'plain', 'utf-8')
msg['From'] = _format_addr(u'rainbow <%s>' % from_addr)
msg['To'] = _format_addr(u'zhang <%s>' % to_addr)
msg['Subject'] = Header(u'Python邮件发送测试', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
