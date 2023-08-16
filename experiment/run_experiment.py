import importlib
import sys

importlib.reload(sys.modules['experiment.behavioural_experiment'])
import experiment.behavioural_experiment

subject_id = 1
session_number = 1

behavioural_experiment(subject_id, session_number)
