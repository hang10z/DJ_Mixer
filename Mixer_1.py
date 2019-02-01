from tkinter import *
import pygame.mixer

app = Tk()
app.title("KEVINS MIX")
app.geometry('250x100+200+100')

sound_file = "50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer
mixer.init()


def shutdown():
    track.stop()
    app.destroy()


track_playing = IntVar()


def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    else:
        track.stop()


track = mixer.Sound(sound_file)

Checkbutton(app, variable = track_playing, command = track_toggle, text = 'START/STOP').pack()
app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()

