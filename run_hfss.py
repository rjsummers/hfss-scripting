import subprocess
import json
import smtplib
import argparse
from email.message import EmailMessage
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

default_odir = Path('data/hfss')

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--project', default='Project1.aedt')
parser.add_argument('-o', '--output', default=default_odir)
args = parser.parse_args()

hfss_params = {}
hfss_params['project_path'] = Path.cwd() / args.project
hfss_params['output_path'] = (Path.cwd() / default_odir /
                              'rectangular_waveguide_HFSSDesign1.s2p')

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('analyze_design_template.py')
template.stream(hfss_params).dump('analyze_design.py')

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
