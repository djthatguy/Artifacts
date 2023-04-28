import urllib.request, urllib.parse, urllib.error
import re
import ssl
iSchoolwebsite = "https://ischool.umd.edu/alumni/alumni-network"
ctx = ssl.create_default_context()
ctx.hostname_checks_common_name = False
ctx.verify_mode = ssl.CERT_NONE
def getHTML(iSchoolwebsite):
    #website = input("Enter 'iSchoolwebsite':") #potential user-input
    iSchoolwebsite = urllib.request.urlopen(url,context=ctx).read()
    return str(iSchoolwebsite).split("\\n")
information = getHTML(iSchoolwebsite)
print(information)
