from modules.scraper.IScraper import IScraper
import dns.resolver

class DnsScraper(IScraper):
  def scrape(self):
    dns_resolver = dns.resolver.Resolver()
    return dns_resolver.nameservers
