# ABC

import re

content=input()
pattern='(A*)(B*)(C*)'

if re.fullmatch(pattern,content):
    print('Yes')
else:
    print('No')
