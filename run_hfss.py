import subprocess
import json
import smtplib
from email.message import EmailMessage

subprocess.run([r'C:\Program Files\AnsysEM\AnsysEM19.4\Win64\ansysedt.exe',
                "-RunScriptAndExit", "analyze_design.py"])

with open("secrets.json") as f:
    email_conf = json.load(f)

msg = EmailMessage()
msg['From'] = email_conf["from"]
msg["To"] = email_conf["to"]
msg['Subject'] = "HFSS Simulation"
email_content = "Your HFSS Simulation recently completed."
msg.set_content(email_content)


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email_conf["from"], email_conf["pass"])
server.send_message(msg)
