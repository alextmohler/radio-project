# radio-project
A collection of python files which cuts up a YouTube video's audio and inserts audio of videos from a YouTube playlist into to and gives back 1 audio file.
It currently only works with the WAN Show podcast by Linus Tech Tips, and any of Jupiter Broadcasting's podcasts. 
Fortunately it is fairly simple to make strainer for timestamps, so feel free to make one for one of the podcasts that you like

# Requirements:
python3 -- the entire thing is written in python3 <br />
ffmpeg -- all of the audio editing/concatenating is done using ffmpeg <br />
youtube-dl -- all of the downloading is done using youtube-dl <br/>
curl -- curl is used to download the YouTube html itself in order to get the timestamps out of the description <br/>

#Output:
Currently the program outputs one .aac file called "output.aac".
It is in the folder "pod\_ep", which is in your current working directory.
