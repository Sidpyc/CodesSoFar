import tkinter
from tkinter import filedialog
import customtkinter as c
from pytube import YouTube
import os
import sys
def start():
    try:
        name=filedialog.askdirectory()
        ytlink=link.get()
        ytobj=YouTube(ytlink, on_progress_callback=onpg)
        title.configure(text=ytobj.title)
        finish.configure(text="")
        if select=="Audio":
            vid=ytobj.streams.get_audio_only()
        else:
            try:
                vid=ytobj.streams.get_highest_resolution()
            except:
                vid=ytobj.streams.get_highest_resolution()
        vid.download(output_path=name)
        finish.configure(text="Downloaded")
    except:
        finish.configure(text="Downlod Error", text_color="red")
def onpg(stream,chunk,bytes_remaining):
    total=stream.filesize 
    bytesdn=total-bytes_remaining
    percentage=(bytesdn/total)*100   
    per=str(int(percentage))
    progress.configure(text=per+"%")
    progress.update()
    pbar.set(float(percentage)/100)
    
    
c.set_appearance_mode("System")
c.set_default_color_theme("blue")

app=c.CTk()
app.geometry("720x480")
app.title("Youtube downloader")
title=c.CTkLabel(app, text="Insert a Youtube Link")
title.pack()
url_var=tkinter.StringVar()
link=c.CTkEntry(app, width=350, height=40,textvariable=url_var)
link.pack(pady=10)
reslst=["Audio","144p", "240p", "360p", "480p", "720p", "1080p"]
res=c.CTkComboBox(app, values=reslst)
select=res.get()
res.pack()
finish=c.CTkLabel(app, text="")
finish.pack()
progress=c.CTkLabel(app, text="0%")
progress.pack()
pbar=c.CTkProgressBar(app, width=400)
pbar.set(0)
pbar.pack()
downloadbtn=c.CTkButton(app, text="Download", command=start)
downloadbtn.pack(pady=20)
#DO NOT TOUCH THIS MANAV
while True:
    app.mainloop()
