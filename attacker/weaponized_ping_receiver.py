from scapy.all import *

pkts = sniff(filter="icmp", timeout =15,count=15)
for packet in pkts:
  if str(packet.getlayer(ICMP).type) == "8": 
    print(packet[IP].src)
