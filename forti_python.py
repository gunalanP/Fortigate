from netmiko import ConnectHandler
import os
from jinja2 import Template
path='C:\\GNS3\\Python\\forti_python'
os.chdir(path)

forti_cred={
    'device_type':'fortinet',
    'host':'172.16.138.187',
    'username':'admin',
    'password':'admin',
    'port':'22',
    'fast_cli': False,
    'global_delay_factor': 2
}

ssh=ConnectHandler(**forti_cred)
ssh.enable()
out=ssh.send_command('show full-configuration ')
file=open('Show_run.txt','a')
file.write(out)