# radio-project
A collection of python files which cuts up a YouTube video's audio and inserts audio of videos from a YouTube playlist into to and gives back 1 audio file.
It currently only works with the WAN Show podcast by Linus Tech Tips, and any of Jupiter Broadcasting's podcasts. 
Fortunately it is fairly simple to make strainer for timestamps, so feel free to make one for one of the podcasts that you like

The project uses ffmpeg to cut up the podcast and inserts the audio of the songs downloaded with youtube-dl.
It uses curl to get the html of the YouTube video in order to get the timestamps out of the YouTube description.
