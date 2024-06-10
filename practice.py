import smtplib
from email.message import EmailMessage

import functions
import main


msg = EmailMessage()
msg.set_content("Hello")

msg['Subject'] = "Test Email"
msg['From'] = 'joebcoding@gmail.com'
msg['To'] = 'joeburrows95@gmail.com'

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()  # Secure the connection
s.login('joebcoding@gmail.com', 'xbhf qyls qwoh wlzq')  # Login to your Gmail account
s.send_message(msg)
s.quit()
