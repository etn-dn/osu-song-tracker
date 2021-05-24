import os
import subprocess
import re

output = os.popen('wmic process where "name=\'osu!.exe\'" get ExecutablePath').read().strip()

if not output:
    print('osu! is currently not running')
else:
    currentSong = None

    while(1):
        out = subprocess.Popen(['tasklist', '/v', '/fo', 'list', '/fi', 'imagename eq osu!.exe'], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()

        # Return title of current song using Regex
        if re.search('Window Title: osu!  - (.*) \[', str(stdout)) is None:
            if (currentSong != ''):
                print('no song playing')
                currentSong = ''
        else:
            songTitle = re.search('Window Title: osu!  - (.*) \[', str(stdout)).group(1)

            if (songTitle != currentSong):
                print(songTitle)
                currentSong = songTitle