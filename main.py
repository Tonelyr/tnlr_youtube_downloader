import youtube_dl
import tkinter as tk

outtmpl = {'outtmpl':'/home/dev/Downloads/%(title)s.%(ext)s',}

def dl(a):
    with youtube_dl.YoutubeDL(outtmpl) as b:
        t = b.download([a])

box1 = tk.Tk()
box1.title("YouTube Video Downloader")
box1.geometry("300x70")

box2 = tk.Entry(box1)
box2.pack(padx=5, pady=5)

def ytl():
    c = box2.get()
    box2.delete(0, "end")
    if len(c) != 0:
        dl(c)
    else:
        print("No")

dl_box = tk.Button(box1, text="Download", command=ytl)
dl_box.pack(padx=5,pady=5)

box1.mainloop()
