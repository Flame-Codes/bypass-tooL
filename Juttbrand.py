import os, platform
try:
        import requests
except:
        os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == "64bit":
        from Jutt import reg
        reg()
elif bit == "32bit":
        from brand import reg
        reg()
