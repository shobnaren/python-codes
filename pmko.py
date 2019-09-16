import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip_addr = "test.rebex.net"
ssh_port = 22
ssh_user = "demo"
ssh_user_pass = "password"
cmd = "ls pub/example"

client.connect(ip_addr, ssh_port, ssh_user, ssh_user_pass, look_for_keys=False, allow_agent=False)

si, so, se = client.exec_command(cmd)
#print(so, se)
out = so.read().decode('utf-8')
client.close()
print(out)
print(len(out.splitlines()))




