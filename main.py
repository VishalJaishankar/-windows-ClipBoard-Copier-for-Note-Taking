from tkinter import Tk
recent=""
i=0
while(1):
    s=Tk().clipboard_get()
    if(recent!=s):
        with open('C:/Users/jaish/Desktop/BlockChain.txt','a') as the_file:
            the_file.write(str(i)+")"+s+"\n")
            i=i+1
        recent=s



