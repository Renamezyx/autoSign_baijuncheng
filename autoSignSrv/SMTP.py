import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# smtp = SMTPTool("1786229908@qq.com",{"title":"hello","context":"hello smtp"})
class SMTPTool():
    my_sender = '2274466264@qq.com'    # 发件人邮箱账号
    my_pass = 'ikkciqwkhouldice'    # 发件人邮箱密码

    def __init__(self, user, ctx):
        self.user = user
        self.ctx = ctx
        self.ret = True

    def send(self):
        try:
            msg = MIMEText(self.ctx["context"], 'plain', 'utf-8')
            # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['From'] = formataddr(["Therzyx", SMTPTool.my_sender])
            # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['To'] = formataddr(["Therzyh", self.user])
            msg['Subject'] = self.ctx["title"]             # 邮件的主题
            server = smtplib.SMTP_SSL(
                "smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            # 括号中对应的是发件人邮箱账号、邮箱密码
            server.login(SMTPTool.my_sender, SMTPTool.my_pass)
            # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.sendmail(SMTPTool.my_sender, [self.user], msg.as_string())
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            self.ret = False