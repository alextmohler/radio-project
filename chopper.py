import os, random
def init(pod_ep):
    """download the YouTube link to an aac, and make apropriate directories for cutting it up, returns path to the aac of the podcast"""
    os.system("youtube-dl --extract-audio --audio-format aac --output pod_ep.aac '" + pod_ep + "'") #downloads the YouTube video
    os.mkdir("pod_ep") #makes general directory
    os.chdir('pod_ep')
    os.system("mv ../pod_ep.aac .") #moves the podcast episode into the general directory for easy chopping
    return os.getcwd()

def chop(wd, ts):
    """Makes a directory, "cuts", and puts the cut up parts of the podcast in it. It needs the path to the directory containing the full episode; and the timestamps in a list"""
    print("Proceeding to chop up the podcast episode.")
    try:
        os.chdir(wd)
    except FileNotFoundError:
        print("The Location provided was not correct, returning None")
        return None

    #making the working directory for the podcast
    os.mkdir('cuts')
    os.chdir("cuts")

    #the loop cuts up the podcast episode according to the timestamps
    sn = 0
    for x in range(len(ts)-1):
        os.system("ffmpeg -loglevel error -i ../pod_ep.aac -ss " + ts[x] + " -to " + ts[x+1] + " " + str(x) + ".aac")
        print("Finished cutting section: " + str(x) + ".aac: " + ts[x] + " to " + ts[x+1] + ".")
        sn = x + 1

    #cut the last section
    os.system("ffmpeg -loglevel error -i ../pod_ep.aac -ss " + ts[-1] + " " + str(sn) + ".aac")
    print("Finished cutting section: " + str(sn) + ".aac: " + ts[-1] + " to end of file.")

def speed_up(wd):
    """needs a directory with aac files only, and then speeds it/them up to 2x with ffmpeg"""
    os.chdir(wd)
    file_list = os.listdir()
    for x in file_list:
        os.system("ffmpeg -loglevel error -i " + str(x) + " -filter:a 'atempo=2.0' -vn s" + str(x))
        os.system("rm " + x)
        print("Finished speeding up section: s" + str(x))
    
def get_songs(pwd, link):
    os.chdir(pwd)
    #check the amount of songs required: the number of podcast segments + 1
    song_num = len(os.listdir()) + 1

    #establish variables
    songs = 0
    csongs = 0
    x = 1

    #make and go into the main directory 
    os.chdir("..")
    os.mkdir("songs")
    os.chdir("songs")

    #while the amount of songs is less then the wanted amount: get another one
    print("Starting to download the songs.")
    while songs < song_num:
        os.system("youtube-dl -q --yes-playlist --playlist-start " + str(x) + " --playlist-end " + str(x) + " --extract-audio --audio-format aac --output song" + str(x) + ".aac '" + link + "'")
        csongs = len(os.listdir())
        if csongs > songs:
            print("Finished downloading song: " + str(x))
            songs += 1
            x += 1

    #get back to the main working directory: "pod_ep"
    os.chdir("..")
        

def concat(wd):
    """needs a working directory with a directory "cuts", and a directory "songs" in it. The contents of said directories should be aac files. It then puts the contents together."""
    try:
        os.chdir(wd)
    except FileNotFoundError:
        print("Error: Incorrect working directory.")
        return None
    
    try:
        os.chdir('cuts')
        os.chdir('..')
        os.chdir('songs')
        os.chdir('..')
    except FileNotFoundError:
        print("Error: The directory 'cuts', or the directory 'songs' was not found.")
        return None

    #make the directory within which to concatenate
    os.mkdir("concat")
    os.chdir("concat")
    
    #establishing variables
    f = open("file_list.txt", 'w') #the list of files for ffmpeg to concatenate
    f_list = [] #the list of files to concatenate; this will end up being written to "file_list.txt"
    sect_num = len(os.listdir('../cuts')) #the number of sections
    used_songs = []
    song_num = 0
    x = 0
    
    while song_num < sect_num:
        pot_file_list = os.listdir("../songs") #a list of what songs are left in the "./songs" directory
        song = random.choice(pot_file_list) #choses randomly from that list
        if song not in used_songs:
            f_list.append("file '" + song + "'") #adds the song to the list
            sect = "s" + str(x) + ".aac" #the podcast section
            f_list.append("file '" + sect + "'") #adds the section of the podcast to the list
            os.system("cp ../cuts/" + sect + " .")
            os.system("cp ../songs/" + song + " .")        
            used_songs.append(song)
            song_num += 1
            x += 1

    #write files to "file_list.txt", and close the file
    f.write("\n".join(f_list))
    f.close()

    #Concatenate the files
    print("Starting Concatenation.")
    os.system("ffmpeg -safe 0 -loglevel error -f concat -i file_list.txt output.aac")
    os.system("mv output.aac ..")
    print("Finished Concatenation.")

def main():
    print("No functions called.")

if __name__ == "__main__":
    main()
