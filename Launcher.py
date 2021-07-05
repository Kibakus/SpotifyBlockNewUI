import os
import requests

with open("BlockTheSpot.bat", "wb") as f: f.write(requests.get("https://raw.githubusercontent.com/mrpond/BlockTheSpot/master/BlockTheSpot.bat").content)
with open("BlockTheSpot.bat", "r") as f: bat = f.read().split("Start-Process -WorkingDirectory $SpotifyDirectory -FilePath $SpotifyExecutable")
text = """
try {
  $webClient.DownloadFile(
    # Remote file URL
    'https://github.com/Kibakus/SpotifyBlockNewUI/raw/main/spotify.exe',
    # Local file path
    "$PWD\spotify.exe"
  )
} catch {
  Write-Output $_
  Sleep
}
Start-Process -FilePath "$PWD\spotify.exe" -Wait
Remove-Item -LiteralPath "$PWD\spotify.exe"
Start-Process -WorkingDirectory $SpotifyDirectory -FilePath $SpotifyExecutable
"""
with open("BlockTheSpot.bat", "w") as f: f.write(bat[0]+text+bat[1])
os.system("START BlockTheSpot.bat")
