import paramiko
import re

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip_addr = "test.rebex.net"
ssh_port = 22
ssh_user = "demo"
ssh_user_pass = "password"
cmd = "ls pub/example/ *.png"

client.connect(ip_addr, ssh_port, ssh_user, ssh_user_pass, look_for_keys=False, allow_agent=False)

si, so, se = client.exec_command(cmd)
#print(so, se)
out = so.read().decode('utf-8')
client.close()
print(out)


#a=[out.splitlines if re.match(r'.png',out)]
#print(re.findall(pattern, out))
print(len(out.splitlines()))
#print(type(out))
