import subprocess

# result = subprocess.run("ipconfig", capture_output=True,text=True)

# result = result.stdout
# a = result.splitlines("")
# print(a)
# for i in a:
#     if i.split():
#         print(i)

# def ping_check(ip):
#     a = subprocess.run("ping "+ip+"",capture_output=True,text=True)
#     output = a.stdout.splitlines()
#     success = False
#     for i in output:
#         if "Lost = 0 (0% loss)" in i:
#             print("ping success",i)
#             success = True
#         if success == True:
#             print("ping success")
#             break
#         else:
#             print("ping failed")
#             break
# ip = input("Enter the ip address to ping: ")
# ping_check(ip)


# import os
# a = os.environ.get("router_ip")
# print(a)

import subprocess
import re

ip = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"

mac = r"([A-F0-9a-f]{2}[:-]){5}[A-F0-9a-f]{2}"

ipv6 = r"[a-f0-9A-f]{1,4}[:]{7}[a-f0-9A-f]"

a = subprocess.run("ipconfig /all",capture_output = True, text = True)
b = a.stdout
print(b)

c = re.findall(ipv6,b)
for ip in c:
    print(".".join(ip))
    