import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
privatekey = paramiko.RSAKey.from_private_key_file("k30_ssh_rbei_dev.key")
ssh.connect(hostname="192.168.1.116",username="root",port=2020,pkey=privatekey)
stdin,stdout,stderr=ssh.exec_command("ifconfig")

a = stdout.read().decode()
print(a)
a = a.splitlines()
for i in a:
    c = i.split()
    for j in c:
        if j == "addr:192.168.1.116":
            print("ip allocated")
ssh.close()








class extreme:
    def __init__(self,a,b):
        self.ip = a
        self.hostname = b
    
    def display(self):
        print(self.ip)
        print(self.hostname)
    
    
e = extreme("192.168.1.1","root")
b = extreme("10.10.10.1","kamalesh")
e.display()