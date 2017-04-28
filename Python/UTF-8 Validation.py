class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return False
        else:
            length = len(data)
            idx = 0
            while idx < length:
                temp = bin(data[idx])[2:]
                if len(temp) < 8:
                    idx += 1
                elif temp.startswith('110'):
                    if idx + 1 < length and ('%08s' % bin(data[idx + 1])[2:]).startswith('10'):
                        idx += 2
                    else:
                        return False
                elif temp.startswith('1110'):
                    if idx + 2 < length and ('%08s' % bin(data[idx + 1])[2:]).startswith('10') and ('%08s' % bin(data[idx + 2])[2:]).startswith('10'):
                        idx += 3
                    else:
                        return False
                elif temp.startswith('11110'):
                    if idx + 3 < length and ('%08s' % bin(data[idx + 1])[2:]).startswith('10') and ('%08s' % bin(data[idx + 2])[2:]).startswith('10') and ('%08s' % bin(data[idx + 3])[2:]).startswith('10'):
                        idx += 4
                    else:
                        return False
                else:
                    return False
            return True
        