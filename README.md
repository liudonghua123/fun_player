# fun_player

This is just a simple terminal windows player for fun. 

I wrote a one line code (`python -c "from ctypes import windll; windll.winmm.mciSendStringW('play music.mid wait', None, 0, None)"`) to play mid music, I found it is interesting, so I make it more complete.

### How to use it

Just download `player.py`, then use python3 to execute it. NO depdences are needed!

You can execute `-h` for some help!

```shell
D:\code\python\fun_player>python player.py -h
usage: player.py [-h] [-m MUSIC]

Play music

options:
  -h, --help            show this help message and exit
  -m MUSIC, --music MUSIC
                        music file to play, support mid, wav, mp3 and so on.

D:\code\python\fun_player>
```

You can play music via `-m music_file_path` to play it immediately, then it will enter a interactive shell, some commands like query(`music`, `info`), set(`music <music_file>`), control(`play`,`pause`,`resume`,`stop`,`exit`) are implemented.

```shell
D:\code\python\fun_player>python player.py -m music.mid
play music.mid
> music     
current music: music.mid
> info
is_playing: True
> help
Please enter some commands like the following
            info: show the current music and status
            music: show the current music
            music <music_file>: set the music file
            play: play the music
            pause: pause the music
            resume: resume the music
            stop: stop the music
            exit|quit: exit the program
            ...

> music mario.mid
stop the current music: music.mid
set the music to mario.mid
command open do not support, need one of ['play', 'pause', 'resume', 'stop', 'close']
set music to mario.mid
> play
execute command: play
play "mario.mid"
> exit

D:\code\python\fun_player>
```

### License

MIT License

Copyright (c) 2022 liudonghua
