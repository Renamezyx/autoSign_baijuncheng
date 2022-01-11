import time
from urllib import parse
print (parse.quote(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
+"123"
)