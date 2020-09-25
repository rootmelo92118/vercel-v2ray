import sys, urllib, os
URL_Parame = sys.argv[1]
core = urllib.request.urlopen("https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip")
with open("core.zip", "wb") as binaryCode:
  binaryCode.write(core.read())
  binaryCode.close()
setupFile = 
