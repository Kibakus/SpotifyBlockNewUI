import os, os.path, shutil, re

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

with open(js, "r", encoding="utf-8") as f:
    jsdata = re.sub(r"&&.\(\)\.createElement\(.{2},{onClick:C,className:.{2}\.Z\.UpgradeButton}\)", "", f.read()).replace("e.ads.leaderboard.isEnabled", "e.ads.leaderboard.isDisabled")
with open(js, "w+", encoding="utf-8") as f:
    f.write(jsdata)

shutil.make_archive(xpui, 'zip', temp)
shutil.rmtree(temp)
shutil.move(fzip, spa)
