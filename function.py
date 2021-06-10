def countwordsfromfile():
    filename=input("enter the file name:")
    nw=0
    file=open(filename,"r")
    for line in file :
        words=line.split()
        nw=nw+len(words)
    print("nw=")
    print(nw)
countwordsfromfile()        