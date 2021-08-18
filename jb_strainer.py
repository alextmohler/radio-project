import os
class show_section(): #makes a class object with the time of the section and the description
    def __init__(self, time, description):
        self.time = time
        self.description = description

def strain_timestamps(s_list):
    """looks for which part of the description has the word 'Chapters', which is where the timestamps are"""
    for s in range(len(s_list)):
        if "Chapters" in s_list[s-1]:
            return s-1

def strain(pod_ep):
    """needs a YouTube link; gives back a list of timestamps"""
    timestamps = []
    e = os.system("curl '" + pod_ep + "' > pod_ep.txt") #curls the youtube html into a file 
    f = open("pod_ep.txt", 'r')
    g = f.read()
    os.system('rm pod_ep.txt')

    #getting only line 21
    h = g.split('\n') 
    i = h[20]

    #grabbing only timestamps, and turning them into a nice list
    j = i.split("shortDescription")
    k = j[1]
    l = k.split("isCrawlable")[0]
    m = l.split("\\n\\n")
    n = strain_timestamps(m)
    o = m[n]
    p = o.split('\\n')
    q = p[1::]
    
    #splitting the timestamps and the description into a class object
    u = []
    for x in q:
        r = x.split(" ")
        s = r[0] #the timestamp
        t = " ".join(r[1::]) #the description
        u.append(show_section(s, t))

    for x in u:
        timestamps.append(x.time)
    return timestamps

def main():
    print(strain(str(input("Enter the YouTube link for the podcast episode: "))))

if __name__ == "__main__":
    main()
