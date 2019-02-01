from tkinter import *
import pygame

mixer = pygame.mixer
mixer.init()

sound_file = "50459_M_RED_Nephlimizer.wav"
track = mixer.Sound(sound_file)


def track_stop():
    track.stop()


def track_start():
    track.play(loops = -1)


app = Tk()
app.title("Kevin's Mix")
app.geometry('250x100+200+100')
stop_button = Button(app, command = track_stop, text = 'STOP')
stop_button.pack(side = RIGHT)
start_button = Button(app, command = track_start, text = 'START' )
start_button.pack(side = LEFT)
app.mainloop()
