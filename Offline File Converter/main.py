import tkinter as tk


import video
from video import videoflix 
import image2
from image2 import run_image_flix
import audio
from audio import run_audio_flix


def open_video():
    window.withdraw
    videoflix()
def open_audio():
    run_audio_flix()

def open_image():
    run_image_flix()

# Create the main window
window = tk.Tk()
window.title("FormatFlix")

# Set the window size
window.geometry("1280x720")

# Set the background color
window.configure(bg="#E8F0F8")




# Create buttons
button_width = 15
button_height = 2
button_font = ('Arial', 12)
button_bg = '#D1E3F9'


image_button = tk.Button(window, text="Image", command=open_image, width=button_width, height=button_height, font=button_font, bg=button_bg)
image_button.pack(pady=10)

video_button = tk.Button(window, text="Video", command=open_video, width=button_width, height=button_height, font=button_font, bg=button_bg)
video_button.pack(pady=10)

audio_button = tk.Button(window, text="Audio", command=open_audio, width=button_width, height=button_height, font=button_font, bg=button_bg)
audio_button.pack(pady=10)





# Start the main loop
window.mainloop()
