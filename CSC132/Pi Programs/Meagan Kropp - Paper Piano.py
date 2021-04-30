########################################
# Name: Meagan Kropp
# Date: May 8, 2020
# Description: Completed paper piano that displays the waves.
########################################
from waveform_vis import WaveformVis
import RPi.GPIO as GPIO
from time import sleep
import pygame
from array import array
from math import sin, pi


# constants
MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

# the note generator class
class Note(pygame.mixer.Sound):
    # note that volume ranges from 0.0 to 1.0
    def __init__(self, wavetype, volume):
        self.frequency = 261.6
        self.wavetype = wavetype
        # initialize the note using an array of samples
        pygame.mixer.Sound.__init__(self, buffer=self.build_samples())
        self.set_volume(volume)


    # builds an array of samples for the current note
    def build_samples(self):
        # calculate the period and amplitude of the note's wave
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
        # initialize the note's samples (using an array of signed 16-bit "shorts")
        samples = array("f", [0] * period)

    
        # generate the square wave
        if self.wavetype == "square":
            for t in range(period):
                if (t < period / 2):
                    samples[t] = amplitude
                else:
                    samples[t] = -amplitude

            vis = WaveformVis()
            vis.visSamples(samples, "Square")  
            return samples

        elif self.wavetype == "sawtooth":
            amp = 1
            amplitude = 0
            for x in range(period):
                if (x < period / 2) :
                    amp += 350
                    samples[x] = amplitude + amp
                else:
                    amplitude = amp * -1
                    amp -= 350
                    samples[x] = amplitude 
                    
            vis = WaveformVis()
            vis.visSamples(samples, "Sawtooth")    
            return samples

        elif self.wavetype == "triangle":
            amp = 1
            amplitude = 0
            for x in range(period):
                if (x < period / 2):
                    if (x < period / 4):
                        amp += 750
                        samples[x] = amplitude + amp
                    else:
                        amp -= 750
                        samples[x] = amp
                else:
                    if (x < period * .75):
                        amp += 700
                        samples[x] = amplitude - amp
                    else:
                        amplitude = amp * -1
                        amp -= 700
                        samples[x] = amplitude
                        
            vis = WaveformVis()
            vis.visSamples(samples, "Triangle")    
            return samples
        


def wait_for_note_start():
    while (True):
        for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
        sleep(0.01)

# waits until a note is released
def wait_for_note_stop(key):
    while (GPIO.input(key)):
        sleep(0.1)


# preset mixer initialization arguments: frequency (44.1K), size
# (16 bits signed), channels (mono), and buffer size (1KB)
# then, initialize the pygame library
pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)


# setup the pin and frequency for the notes
keys = [ 20, 16, 12, 26 ]
freqs = [ 261.6, 261.6, 261.6, 261.6]
notes = []
wavetype = ["square", "sawtooth", "triangle"]

# setup the input pin
GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)

# create the actual notes
for n in range(len(wavetype)):
    notes.append(Note(wavetype[n], 1))
    
# the main part of the program
print "Welcome to Paper Piano!"
print "Press Ctrl+C to exit..."

# detect when Ctrl+C is pressed so that we can reset the GPIO pins
try:
    while (True):
        # play a note when pressed...until released
        key = wait_for_note_start()
        notes[key].play(-1)
        wait_for_note_stop(keys[key])
        notes[key].stop()
except KeyboardInterrupt:
    # reset the GPIO pins
    GPIO.cleanup()






