import importlib
import sys
from behavioural_experiment import main

importlib.reload(sys.modules['behavioural_experiment'])

subject_id = 5
session_number = 1

main(subject_id, session_number)