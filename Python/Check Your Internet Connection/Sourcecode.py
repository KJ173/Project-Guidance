import urllib
from urllib.request import urlopen
def connectionCheck():
    try:


        urlopen('https://www.google.com',timeout=1)
        return True
    except urllib.error.URLError as Error:
        return False

if connectionCheck():
    print("Yes your internet is connected")
else:
    print("opps!😅 your internet is not connected with your System")