
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

 