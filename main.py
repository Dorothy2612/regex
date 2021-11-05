import re
import os
##Use regex to search for specific strings within the output of os object.
if __name__ == '__main__':
    a=re.compile("8")
    v=str(os.environ)
    print(a.findall(v))
    print(os.environ)