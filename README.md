# Simple-discord-bot
This bot runs 2 commands
## Music commands:
* !play - searches the song on youtube and plays it in your current vc channel
* !pause - pauses the current playing song
* !resume - resume the song after its been paused
* !skip - skips the current song being played
* !queue - displays the current music queue
## Image commands:
* !search - will search the given (input) keyword
* !get - will get the image based on the most current search

## bot.py
Responsible for managing all the discord API tings

## Install libraries
> pip install -r requirements.txt

or

> pip install discord.py[voice] pip install youtube_dl

### To install google_images_download:
git clone https://github.com/Joeclinton1/google-images-download.git cd google-images-download && python setup.py install

### To install ffmpeg (windows):
Head over to https://www.gyan.dev/ffmpeg/builds/ and download **ffmpeg-git-full.7z** to install. Add path into your environment variables for easy access. 
