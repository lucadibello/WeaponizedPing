
class Checksum:

  @staticmethod
  def calculate(data: str) -> int:
    # In this function we make the checksum of our packet 
    str_ = bytearray(data)
    csum = 0
    countTo = (len(str_) // 2) * 2

    for count in range(0, countTo, 2):
      thisVal = str_[count+1] * 256 + str_[count]
      csum = csum + thisVal
      csum = csum & 0xffffffff

    if countTo < len(str_):
      csum = csum + str_[-1]
      csum = csum & 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer