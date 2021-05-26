import os
import os.path
import shutil
import re
import requests
import subprocess

if "y" in input("Download BlockTheSpot script (Mrpond) (Y)es/(N)o\n").lower():
    with open("temp.bat", "wb") as f:  # run skript BlockTheSpot (mrpond)
        f.write(requests.get("https://raw.githubusercontent.com/mrpond/BlockTheSpot/master/BlockTheSpot.bat").content)
    subprocess.Popen("temp.bat", stdin=subprocess.PIPE).communicate(input=b'\n')
    os.remove("temp.bat")

os.system("taskkill /F /IM Spotify.exe")  # close Spotify
os.system("cls")


PATH = os.getenv('APPDATA') + r"\Spotify\Apps"
xpui = os.path.join(PATH, "xpui")
spa = os.path.join(PATH, "xpui.spa")
bak = os.path.join(PATH, "xpui.bak")
fzip = os.path.join(PATH, "xpui.zip")
temp = os.path.join(PATH, "temp")
js = os.path.join(temp, "xpui.js")

if os.path.exists(spa) is False:
    exit()
if os.path.exists(bak):
    os.remove(bak)

shutil.copy(spa, bak)
shutil.move(spa, fzip)
shutil.unpack_archive(fzip, temp, "zip")

try:
    with open(js, "r", encoding="utf-8") as f:
        jsdata = f.read()
        UB = re.findall(r"1024&&(.+?UpgradeButton}\),)", jsdata)[0]
        LB = re.findall(r"\w+\.ads\.leaderboard\.isEnabled", jsdata)[0]
        LBedit = LB.replace("isEnabled", "isDisabled")
    with open(js, "w+", encoding="utf-8") as f:
        f.write(jsdata.replace(UB, "").replace(LB, LBedit))
except IndexError:
    print("I did not find a button or empty block")

shutil.make_archive(xpui, 'zip', temp)
shutil.rmtree(temp)
shutil.move(fzip, spa)
os.system(f"START {os.getenv('APPDATA')}\\Spotify\\Spotify.exe")

