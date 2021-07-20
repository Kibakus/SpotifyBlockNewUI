@echo off
powershell -Command "& {Invoke-WebRequest -UseBasicParsing 'https://raw.githubusercontent.com/mrpond/BlockTheSpot/master/install.ps1' | Invoke-Expression}"
powershell -Command "& {get-process | where { $_.processname -eq 'Spotify' } | Stop-Process -Force ; get-process | where { $_.processname -eq 'SpotifyWebHelper' } | Stop-Process -Force ; Invoke-WebRequest -Uri 'https://github.com/Kibakus/SpotifyBlockNewUI/raw/main/spotify.exe' -OutFile $PWD'\spotify.exe' ; Start-Process -Filepath $PWD'\spotify.exe' -Wait ; Remove-Item $PWD'\spotify.exe' ; Start-Process -WorkingDirectory $env:APPDATA'\Spotify' -FilePath $env:APPDATA'\Spotify\Spotify.exe'}"
pause
exit