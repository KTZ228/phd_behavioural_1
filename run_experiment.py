import importlib
import sys
import scripts.behavioural_experiment as behavioural_experiment

import psychopy
psychopy.useVersion('2022.1.0')
from psychopy import visual, core, event

importlib.reload(sys.modules['scripts.behavioural_experiment'])

subject_id = 5
session_number = 1

#behavioural_experiment.main(subject_id, session_number)

# Trial variables
n_blocks = 8
n_trials_per_block = 12
ibi_seconds = [21,24] # inter-block-interval
iti_seconds = [2,3,4] # inter-trial-interval

stimulus_presentation_milliseconds = [500,7000]
outcome_screen_seconds = [2,3]


# From this point on the script will be shown in a long format
win = visual.Window(fullscr = 1, units = 'norm')
msg = visual.TextStim(win, text=u'\u00A1Hola mundo!', pos=(0,0))
fixation_cross = visual.ShapeStim(
        win=win, name='polygon', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)

fixation_cross.draw()
win.flip()
core.wait(1)
win.close()

'''
Set-up:
    Explanation first. The participant should push the joystick forward or backwards based on the presented stimuli.
    Feedback will be provided after every trial so notify the participant of when the reward changes (volatility).
    Show fixation cross during iti.
    
    reward/punishment in the form of a monetary reward
'''