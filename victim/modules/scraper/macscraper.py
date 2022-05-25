from modules.scraper.IScraper import IScraper


import uuid

class MacScraper (IScraper):
  def scrape(self) -> str:
    # Calculate MAC address
    mac = uuid.getnode()
    mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    return mac
