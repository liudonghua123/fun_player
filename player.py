#!/usr/bin/env python3
# coding: utf-8

from ctypes import windll
import argparse
import os
import re
import signal

# https://docs.python.org/3/library/argparse.html
# use argparse to parse the command line arguments
parser = argparse.ArgumentParser(description='Play music')
parser.add_argument('-m', "--music",
                    help='music file to play, support mid, wav, mp3 and so on.')
args = parser.parse_args()
music = args.music

# check if the music file exists
if music == None or not os.path.exists(music):
    print(f"File {music} does not exist.")
    print(f"Try to set the music file with command 'music <music_file>'. in the following interactive shell.")
    print(f"Enter 'help' to get more information.")

# use winmm module of ctypes, see https://docs.python.org/3/library/ctypes.html
# the winmm module is a wrapper of the winmm.dll
winmm = windll.winmm

# define the support commands
support_commands = ['play', 'pause', 'resume', 'stop', 'close']

class Player:
    '''
    A lightweight windows player, support play, pause, resume, stop functions.
    It use winmm.mciSendStringW to control the system player internally.
    '''

    def __init__(self, music):
        self._music = music
        self._is_playing = False

    @property
    def music(self):
        return self._music

    @music.setter
    def music(self, music):
        # Try to quotes the music file name for safe
        self._music = f'"{music}"'

    @property
    def is_playing(self):
        return self._is_playing

    def _do_command(self, command):
        # see https://learn.microsoft.com/en-us/previous-versions/dd757161(v=vs.85)
        # https://learn.microsoft.com/en-us/windows/win32/multimedia/multimedia-command-strings?redirectedfrom=MSDN
        # see also PlaySound https://learn.microsoft.com/en-us/previous-versions/dd743680(v=vs.85)
        winmm.mciSendStringW(f'{command} {self.music}', None, 0, 0)

    def play(self):
        print(f'play {self.music}')
        self._do_command('open')
        self._do_command('play')
        self._is_playing = True

    def pause(self):
        print(f'pause {self.music}')
        self._do_command('pause')
        self._is_playing = False

    def resume(self):
        self._do_command('resume')
        self._is_playing = True

    def stop(self):
        self._do_command('stop')
        self._is_playing = False

    def call(self, command: str):
        if not command in support_commands:
            print(
                f'command {command} do not support, need one of {support_commands}')
            return
        # check if the [command] function exists, invoke it.
        # The [command] function can be defined with customization
        if hasattr(self, command) and callable(func := getattr(self, command)):
            func()
        else:
            self._do_command(command)


def main():
    def handler(signum, frame):
        print('Bye, have a nice day!')
        exit(0)
    # handle the Ctrl+C signal, just exit
    signal.signal(signal.SIGINT, handler)

    global music
    player = Player(music)
    if music != None and os.path.exists(music):
        player.play()
    command_music_pattern = re.compile(r'(?P<command>.*)\s+(?P<music>.*)')
    # make an interactive shell
    while True:
        command = input('> ')
        command_music_match = command_music_pattern.match(command)
        if command in ['exit', 'quit']:
            player.call('close')
            break
        elif command == 'help':
            print(f'''Please enter some commands like the following
            info: show the current music and status
            music: show the current music
            music <music_file>: set the music file
            play: play the music
            pause: pause the music
            resume: resume the music
            stop: stop the music
            exit|quit: exit the program
            ...
            ''')
            continue
        elif command == 'info':
            print(f'is_playing: {player.is_playing}')
        elif command == 'music':
            print(f'current music: {player.music}')
        elif command in support_commands:
            print(f'execute command: {command}')
            player.call(command)
        elif command_music_match:
            command = command_music_match.group('command')
            music = command_music_match.group('music')
            if command == "music" and music != player.music:
                # check whether the music is playing
                if player.is_playing:
                    print(f'stop the current music: {player.music}')
                    player.call('stop')
                    player.call('close')
                print(f'set the music to {music}')
                player.music = music
                player.call('open')
                print(f'set music to {music}')
            # TODO: other commands with music are not support now.
            # print(f'execute command: {command}')
            # player.call(command)


if __name__ == '__main__':
    main()
