import os
class show_section():
    def __init__(self, time, description):
        self.time = time
        self.description = description

def strain(pod_ep):
    timestamps = []
    """needs a YouTube link to podcast, returns a list of timestamps"""
    e = os.system("curl '" + pod_ep + "' > pod_ep.txt") #curls the youtube html into a file
    f = open("pod_ep.txt", 'r')
    g = f.read()
    os.system('rm pod_ep.txt')

    #getting only line 21, which is where the description is
    h = g.split('\n') 
    i = h[20]

    #grabbing only timestamps, and turning them into a nice list
    j = i.split("Timestamps")
    k = j[2]
    m = k.split("}")[0].strip()
    n = m.split('\\n')
    bracketed = False
    for x in n:
        if "[" in x:
            bracketed = True
    
    #straining out timestamps, bracketed or not
    bracketed_list = [] #we need a permanent variable to store the show sections, not one in a if statement
    unbracketed_list = [] #need permanent variable, see above

    if bracketed == True:
        print("Bracketed.")
        o = []
        for x in n:
            if "[" in x: #the important ones have been bracketed by LTT hence having "["
                o.append(x)
        #splitting the timestamps and descriptions
        for x in o:
            p = x.split("]")
            q = p[0].strip("[")
            r = p[1].strip()
            bracketed_list.append(show_section(q, r))

        for x in bracketed_list:
            timestamps.append(x.time)

    else:
        print("Not Bracketed.")
        for x in n:
            o = x.split(" ")
            p = o[0] #the timestamp
            q = " ".join(o[1::]) #the description
            unbracketed_list.append(show_section(p, q))

        for x in unbracketed_list:
            timestamps.append(x.time)

    return timestamps

def main():
    print(strain(str(input("Enter the YouTube link for the podcast episode: "))))

if __name__ == "__main__":
    main()
