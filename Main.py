from tkinter import *
from pygame import mixer
import os

# Function to play the song
def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()

# Function to pause the song
def pausesong():
    mixer.music.pause()

# Function to stop song
def stopsong():
    mixer.music.stop()
# Function to resume after stopping the song
def resumesong():
    mixer.music.unpause()


root = Tk()
root.title("Webpage title")
mixer.init()
playlist = Listbox(root, selectmode=SINGLE, bg="black")
playlist.grid(columnspan=5)
os.chdir('path/to/dir/')
song_list = os.listdir()
for song in song_list:
    playlist.insert(END, song)

# Buttons for playing, pause etc
Button(root, text="play", command=playsong).grid(row=1, column=0)
Button(root, text="pause", command=pausesong).grid(row=1, column=1)
Button(root, text="stop", command=stopsong).grid(row=1, column=2)
Button(root, text="resume", command=resumesong).grid(row=1, column=3)

# Loop to run the entire functions
mainloop()
