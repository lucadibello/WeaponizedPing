import struct
import time
import sys
from socket import htons
from modules.cipher.RSACipher import RSACipher
from modules.payload import Checksum

class Payload:
  HEADER_CONTENT= "bbHHh" # 62 62 48 48 68
  ICMP_ECHO_REQUEST = 8
  __MAX_SIZE = 1472

  def __init__(self, header: bytes, data: bytes, id: int):
    self.header = header
    self.data = data
    self.id = id

  @staticmethod
  def build_basic_imcp_header (id: int, checksum = 0) -> bytes:
    return struct.pack(Payload.HEADER_CONTENT, Payload.ICMP_ECHO_REQUEST, 0, checksum, id, 1)

  @staticmethod
  def build_basic_imcp_data () -> bytes:
    return struct.pack("d", time.time())

  def build_payload(self, *data: str) -> bytes:
    # Calculate how much space is left in the packet
    remainingBytes = self.__MAX_SIZE - struct.calcsize("d")

    # Append each string to the data buffer until the maximum size is reached
    fullStr = ""
    for idx, string in enumerate(data):
      if len(string) > remainingBytes:
        raise ValueError("String is too large to fit in the packet")

      # Check if last index
      if idx == len(data) - 1:
        fullStr += string
      else:
        fullStr += string + "|"

    print(fullStr)
    
    encodedData = RSACipher.encrypt(fullStr)
    print("ENCODED:")
    print(encodedData)
    self.data += encodedData
    remainingBytes -= len(encodedData)
    
    # Calculate the checksum on the data and the dummy header.
    tempChecksum = Checksum.calculate(self.header + self.data)

    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
      #Convert 16-bit integers from host to network byte order.
      tempChecksum = htons(tempChecksum) & 0xffff
    else:
      tempChecksum = htons(tempChecksum)

    # Build new header with the correct checksum
    self.header = Payload.build_basic_imcp_header(self.id, tempChecksum)

    # Now build the packet
    return self.header + self.data

