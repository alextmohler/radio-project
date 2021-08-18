import chopper, jb_strainer, wan_strainer
def main():
    #initialize variables
    _type = str(input("Enter the podcast type [wan/jb]: ")).strip() #type of podcast: 'wan' for the WAN Show, or 'jb' for most of Jupiter Broadcasting's shows
    pod_ep = str(input("Enter the YouTube link for the podcast: ")).strip() #the YouTube link for the podcast episode
    playlist = str(input("Enter the YouTube link for the music playlist: ")).strip() #the link to the YouTube playlist
    timestamps = []

    #straining out the timestamps according to which type of podcast is entered
    if _type == "wan":
        timestamps = wan_strainer.strain(pod_ep)

    elif _type == "jb":
        timestamps = jb_strainer.strain(pod_ep)
    
    else:
        print("Please enter either 'wan' for the WAN Show, or 'jb' for most of Jupiter Broadcasting's shows")
        return None

    #chopping up the podcast into bits
    init = chopper.init(pod_ep)
    if init == None:
        return None
    else:
        chopper.chop(init, timestamps)

    #speeding up the bits of the podcast
    print("Proceeding to speed up the podcast.")
    chopper.speed_up('.')

    #downloading songs
    print("Downloading songs.")
    chopper.get_songs(".", playlist)
    
    #concatenating the songs and podcast bits
    print("Concatenating the songs and podcast bits.")
    chopper.concat(".")
    

if __name__ == "__main__":
    main()
