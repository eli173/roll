
import sys
from random import randint


def roll(s):
    d = s.index("d")
    fore = s[:d]
    aft = s[d+1:]
    num = int(fore)
    sz = int(aft)
    tot = 0
    for i in range(num):
        tot += randint(1,sz)
    return str(tot)
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: 'roll 3d6' to roll 3 d6\n\
        Example: 'roll 2d6 3d10' rolls 2 d6, 3 d10, and gives results separately")
        exit(0)
    retstr = ""
    for s in sys.argv[1:]:
        retstr += roll(s) + " "
    print(retstr)
        
