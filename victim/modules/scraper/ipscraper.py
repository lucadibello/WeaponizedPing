from modules.scraper.IScraper import IScraper

class IpScraper (IScraper):
  def scrape(self):
    # Get public ip address
    import requests
    ip = requests.get('https://api.ipify.org').text
    return ip
      