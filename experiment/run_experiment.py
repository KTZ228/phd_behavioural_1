import importlib
import sys
from experiment import behavioural_experiment

importlib.reload(sys.modules['experiment.behavioural_experiment'])

subject_id = 1
session_number = 1

behavioural_experiment.main(subject_id, session_number)