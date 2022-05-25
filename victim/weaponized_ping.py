import argparse
from modules import Pinger

# using argsparse, request an ip address from the user
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="IP address to ping", required=True)
args = parser.parse_args()

# main method
def main():
    # instantiate the Pinger class
    pinger = Pinger(args.ip)
    # call the ping method
    pinger.ping()
    # notify the user that the ping has been sent
    print("[!] Ping sent succesfully to " + args.ip)

if __name__ == "__main__":
  # Validate IP address set by the user, if valid, execute main, otherwise print error and exit
  try:
    ip = args.ip
    ip = ip.split('.')
    if len(ip) != 4:
      raise ValueError("Invalid IP address")
    for i in ip:
      if not i.isdigit():
        raise ValueError("Invalid IP address")
    main()
  except ValueError as e:
    print(e)