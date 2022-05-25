from modules.scraper.IScraper import IScraper
import netifaces

class InterfaceScraper (IScraper):
  def scrape(self):
    # Scrape machine to read network information such as DHCP, DNS, Default Gateway, Machine Name and Subnet Mask

    # Fetch all the available interfaces
    interfaces = netifaces.interfaces()

    # Fetch all the available addresses from wifi or ethernet interfaces (not loopback or bridge)
    addresses = {}
    for interface in interfaces:
      # If interface starts with lo or br, skip it
      if interface.startswith("lo") or interface.startswith("br") or interface.startswith("gif") or interface.startswith("ap") or interface.startswith("stf") or interface.startswith("utun") or interface.startswith("pktap"):
        continue
      try:
        addresses[interface] = netifaces.ifaddresses(interface)[netifaces.AF_INET]
      except:
        addresses[interface] = netifaces.ifaddresses(interface)[18] 
    # Return addreses
    return addresses
