#! /usr/bin/python3

import paramiko
import time
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# { ip / port / username / password}
client.connect("10.10.10.100", 22, "cisco", "cisco")
# send commands
print("You have logged into the router.")
commands = client.invoke_shell()
#  commands.send("terminal length 0 \n")
print("You have invoked the shell.")
time.sleep(.5)
commands.send("enable\n")
time.sleep(.5)
commands.send("terminal length 0\n")
time.sleep(.5)
commands.send("show ip interface brief\n")
time.sleep(1)
print("The version request has been sent.")
# retrieve and print output
output = commands.recv(65535)
output = output.decode("utf-8")
time.sleep(1)
print(output)   # commands

time.sleep(1)
client.close()


