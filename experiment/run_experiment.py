import importlib
import sys
from experiment.behavioural_experiment import test_function

importlib.reload(sys.modules['experiment.behavioural_experiment'])

subject_id = 5
session_number = 1

test_function(subject_id, session_number)