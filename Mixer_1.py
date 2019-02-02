from tkinter import *
import pygame.mixer

app = Tk()
app.title("KEVINS MIX")

sound_file = "50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer
mixer.init()


def shutdown():
    track.stop()
    app.destroy()


def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    else:
        track.stop()


volume = DoubleVar()

# The 'v' that is passed into this method is the volume float value from the slider.
# Then set the value of volume to the set_volume() method which is built into pygame
def change_volume(v):
    track.set_volume(volume.get())


track = mixer.Sound(sound_file)
track_playing = IntVar()
Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file).pack()

volume_scale = Scale(app, variable = volume, from_ = 0.0, to = 1.0, resolution = .01, command = change_volume, label = 'Volume', orient = HORIZONTAL )
volume_scale.pack(side = RIGHT)

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()

