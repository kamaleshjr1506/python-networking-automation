
a = ['a','b','c','d']
b = [1,2,3,4]
c = {}
for i in range (len(a)):
    c[a[i]] = b[i]
print(c)

#Remove Duplicate elements from the string
a  = "kamalesh"
b = []
for i in a:
    if i not in b:
        b.append(i)
c = "".join(b)
print(c)


#Reverse the string
a  = "kamalesh"
b = ""
for i in a:
    b = i+b
print(b)
c   = a[::-1]
print(c)

a = "my name is kamalesh "
b = ""
a = a.split()
for i in a:
    b = b + i[::-1] + " "
print(b)



#Lambda
x = lambda a:a+10
print(x(5))


a= "kamalesh"
output={"i":2,"n":1,"d":1,"a":1}
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
print(b)


a = "1,2,3-5,6,3-7"
outpt = "1,2,3,4,5,6,3,4,5,6,7"
k = []
b = a.split(",")
for i in b:
    if "-" in i:
        c = i.split("-")
        for i in range(int(c[0]),int(c[1])+1):
            k.append(i)
    else:
        k.append(int(i))
print(k)

b = a.split(",")
print(b)
for i in b:
    if "-" in i:
        start,end = i.split("-")
        #print(start,end)
        for i in range(int(start), int(end)+1):
            print(i)
    else:
        print(i)
        

l1 = [1,2,3]
l2 = ["A","B","C"]

c = {}

c[l1[0]]= l2[1]
print(c)

a = {"apple":"carrot","banana":"potato","orange":"cabbage"}
b = "i have one apple, three banana, two orange and one grapes"
c = b.split(",")
d = []
for i in c:
    for j,k in a.items():
        if j in i:
            m = i.replace(j,k)
            d.append(m)
l = ",".join(d)
print(l)


a = [2,5,6,21,2,534,23]
m = a[0]

for i in a:
    if i < m:
        m = i
        i = m
print(m)


a= [1,2,3,3,3,4,4,5,6,7,7,7,9,3,4,10,11,11]

b = ""
c = []
for i in a:
    if i != b:
        c.append(i)
        b = i
print(c)


a = "kamalesh"
b = "samantha"
#out = klnet
c = []
for i in a:
    if i not in c:
        c.append(i)
for j in b:
    if j not in c:  
        c.append(j)
    else:
        c.remove(j)
print(c)

result  = 100/777
sam  = "edewfe"
#print("the mark is {r:0.3f}".format(r=result))
print(f"the result is {result} {sam}")




a = [20,3,4,5,10,1,0]
maxx = a[0]
for i in a:
    if i < maxx:
        maxx = i
print(maxx)

import datetime
from sre_constants import FAILURE


a = 0
while a <10:
    x = datetime.datetime.now()
    print(f"current date and time is {x}")
    a+=1
else:
    print("kaalesh")

def kamalesh():
    print("kamaleshssssssssssssss")
    c = 1
    return c

kamalesh()


a = "kamalesh"
b = "samantha"
c = a + b
unique_chars = []

for ch in c:
    if c.count(ch) == 1:
        unique_chars.append(ch)

print(unique_chars)


class Sample:
    def __init__(self):
        pass

    def display(self):
        a= "kamales"
        return a


import copy

a = [[1,99]]

shallow1 = copy.copy(a)
shallow1[0][0]  = [0]

print(a)
print(shallow1)

a = [[1,99]]

shallow1 = copy.deepcopy(a)
shallow1[0][0]  = [0]

print(a)
print(shallow1)

# # Without using for loop we can execute using map function
# number = 1,2,3
# def a(x):
#     print(x*2)
# (list(map(a,number)))


a = "01mdoew325345refek4256347"
b = ""
c = ""
for i in a:
    if not i.isdigit():
        b = b+i
    else:
        c = c+i
print(c)




a = "my name is kamalesh "
b = ""
d = []
for i in a:
    b = i+b
c = b.split()
print(" ".join(c[::-1]))


a = """Network Destination        Netmask          Gateway       Interface  Metric 
           0.0.0.0          0.0.0.0     192.168.18.1     192.168.18.4     35 
         127.0.0.0        255.0.0.0         On-link         127.0.0.1    331 
         127.0.0.1  255.255.255.255         On-link         127.0.0.1    331 
   127.255.255.255  255.255.255.255         On-link         127.0.0.1    331 
      192.168.18.0    255.255.255.0         On-link      192.168.18.4    291 
      192.168.18.4  255.255.255.255         On-link      192.168.18.4    291"""
      
      
b = a.strip("").split("\n")

for i in b[1:]:
    c = i.split()
    d = c[4]
    if int(d) <=291:
        print(i)






a= """Router# show ip bgp
BGP table version is 10, main routing table version 10
Local router ID is 192.168.1.1, local AS is 65000

Status codes: s suppressed, d damped, h history, * valid, > best, i internal
Origin codes: i IGP, e EGP, ? incomplete

   Network           Next Hop        Metric  LocPrf  Weight  Path
*> 10.0.0.0/8        192.168.1.2     0       100     32768   i
*> 172.16.0.0/16     0.0.0.0         0       100     32768   i
*> 192.168.1.0/24    0.0.0.0         0       100     32768   i
"""

b = a.strip().split("\n")

for i in b[8:]:
    print(i)



a = "aaabbbbcccdewfeew"
res = ""
count = 1
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        count = count+1
    else:
        res = res +str(a[i-1]) + str(count)
        count = 1
res = res +str(a[-1]) + str(count)
print(res)



students = {
    'student1': {
        'name': 'Drake',
        'age': 20,
        'grade': 'A'
    },
    'student2': {
        'name': 'Travis',
        'age': 22,
        'grade': 'B'
    },
    'student3': {
        'name': 'Charlie',
        'age': 21,
        'grade': 'A+'
    }
}


a = """Interface            Lanes    Speed    MTU    FEC    Alias    Vlan    Oper    Admin        Type    Asym PFC
-----------  ---------------  -------  -----  -----  -------  ------  ------  -------  ----------  ----------
  Ethernet0          1,2,3,4     100G   9100     rs   Eth1/1   trunk      up       up      QSFP28         N/A
  Ethernet4          5,6,7,8     100G   9100     rs   Eth2/1  hybrid    down       up         N/A         N/A
  Ethernet8       9,10,11,12     100G   9100     rs   Eth3/1  hybrid    down       up         N/A         N/A"""

b = a.splitlines(",")
for i in b:
    if "up" in i:
        d = i.split()
        print(d[7],d[8])

 

a = """192.168.1.45 - - [09/Jun/2026:10:14:22 +0000] "GET /images/logo.png HTTP/1.1" 404 1543
2001:db8:85a3:8d3:1319:8a2e:370:7348 - - [09/Jun/2026:10:14:35 +0000] "POST /api/v1/login HTTP/1.1" 401 230
10.0.0.12 - - [09/Jun/2026:10:15:01 +0000] "GET /checkout HTTP/1.1" 500 5230
192.168.1.99 - - [09/Jun/2026:10:15:22 +0000] "GET /wp-admin/ HTTP/1.1" 403 412
2001:db8:85a3:8d3:1319:8a2e:370:7348 - - [09/Jun/2026:10:16:05 +0000] "POST /api/v1/login HTTP/1.1" 401 230
172.16.254.1 - - [09/Jun/2026:10:16:40 +0000] "GET /index.html HTTP/1.1" 404 1543
10.0.0.12 - - [09/Jun/2026:10:17:12 +0000] "GET /checkout HTTP/1.1" 500 5230
3a2f:6b88:fe12:0000:0000:0000:abcd:1234 - - [09/Jun/2026:10:17:55 +0000] "GET /api/v2/users HTTP/1.1" 503 1205
192.168.1.45 - - [09/Jun/2026:10:18:10 +0000] "GET /images/favicon.ico HTTP/1.1" 404 1543
2001:db8:85a3:8d3:1319:8a2e:370:7348 - - [09/Jun/2026:10:18:15 +0000] "POST /api/v1/login HTTP/1.1" 401 230
10.0.0.12 - - [09/Jun/2026:10:19:00 +0000] "GET /checkout HTTP/1.1" 500 5230
192.168.1.45 - - [09/Jun/2026:10:19:30 +0000] "GET /broken-link HTTP/1.1" 404 1543
3a2f:6b88:fe12:0000:0000:0000:abcd:1234 - - [09/Jun/2026:10:20:02 +0000] "GET /api/v2/users HTTP/1.1" 503 1205
172.16.254.1 - - [09/Jun/2026:10:20:15 +0000] "GET /hidden-directory HTTP/1.1" 403 412
192.168.1.45 - - [09/Jun/2026:10:21:00 +0000] "GET /images/logo.png HTTP/1.1" 404 1543"""







# when designing a system test plan for an enterprise switch deployed in a enterprise core layer,
 
# how do you determine the scale limits (e.g., maximum VLANs, MAC table size, ARP table size)? 

# How would you automate the validation of the system's behavior when these tables overflow ?

error_codes = {404:"not found",401:"unautorized",403:"Fobidden",500:"internalservererror"}
error_codes = [404,401,403,500]

a = a.splitlines()
for i in a:
    b =i.split()
    print(b)
    # for i in error codes:
    #     index = b.index(i)
    # if b in error_codes:
    #     print(b[0])
            
            

#Find the missing number in a sequence of integers from 1 to n, where one number is missing. The input is a list of integers containing n-1 numbers from the range 1 to n.

n = 10
a = [1,2,3,4,5,6,7,8,10]
expected_sum = n * (n + 1) // 2 
actual_sum = sum(a)
missing_number = expected_sum - actual_sum
print("The missing number is:", missing_number)


# Write a Python program that:
# Takes a router IP address as input ip 
# Validates the IP format
# Pings the router to check reachability
# Logs into the router using credentials stored in environment variables
# Executes: show interfaces
# Uses regex to verify that all interfaces are in “up/up” state
# Returns:
# SUCCESS if all interfaces are up
# FAILURE otherwise


import os
a = os.environ.get("router_ip")
print(a)



a = [1,2,3,4,6,5,7,9,10]
n = 100
missing = []

for i in range(1,n+1):
    if i not in a:
        missing.append(i)
        
print(missing)


###### Second Largest Number in a List
a = [25, 8, 45, 67, 89, 21, 89, 65]
fla = a[0]
sla = a[0]

for i in a:
    if i >fla:
        fla = i
for i in a:
    if fla != i and i>sla:
        sla = i
print(sla)







# ips = ["10.1.1.1","10.1.1.2","10.1.1.1","10.1.1.3","10.1.1.2"]
 
# #output = {"10.1.1.1":2,"10.1.1.2":2,"10.1.1.3":1} 

# b = {}

# for i in ips:
#     if i in b:
#         b[i] +=1
#     else:
#         b[i] = 1
        
# print(b)

# data=[10,20,10,30,20]
# out = []
# for i in data:
#     if i not in out:
#         out.append(i)
# print(out)
# import os
# os.toch("file.xtx")



# # with open("File.txt","r+") as f:
# #     f.read()
    
    
    
# # Input  = "robot framework automation testing"

# # a = Input.split()
# # leenn = len(a[0])
# # # print(leenn)

# # for i in a:
# #     tmp = 0
# #     b = len(i)
# #     #print(b)
# #     if b > tmp:
# #         tmp = b
        
# #     print(tmp)
        
    
# # a = [1,2,3,4,5]


# # data = {
# #     "devices": [
# #       {"hostname":"sw1","ip":"10.1.1.1"},
# #       {"hostname":"sw2","ip":"10.1.1.2"},
# #       {"hostname":"sw3","ip":"10.1.1.3"}
# #     ]
# # }

# # len = len(data["devices"])
# # print(data["devices"][0])
# # aaaa = []
# # for i in data["devices"]:
# #     aaaa.append(i["hostname"])
    
# # print(aaaa)


# import subprocess

# ip = ["127.0.0.1","127.0.0.3","127.0.0.2"]

# a= subprocess.run("ping google.com",capture_output = True,text = True)

# print(a.returncode)
    
    
    
 


a = "robot is an automation2222 frameworkwdewceded"
a = a.split()
longe = a[0]
for i in a:
    if len(i) > len(longe):
        longe = i
print(longe)