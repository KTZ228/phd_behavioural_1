import argparse
import textwrap
import sys

def parseArguments(argv):

    usage_text = textwrap.dedent('''

This is a test.
    Subject_ID accepts an integer.
    Session_number accepts an integer.
    
    ''')

    parser = argparse.ArgumentParser(
        prog="behavioural_experiment",usage=usage_text)

    parser.add_argument('--subject_id', type=int, nargs='?', help='''Subject ID. This is necessary to run the experiment.''')
    parser.add_argument('--session_number', type=int, nargs='?', help='''Session number. This is required to run the experiment.''')

    args=parser.parse_args(argv)

    if args.subject_id is None:
        parser.print_help()
    exit()

    return args

def main():
    args = parseArguments(sys.argv[1:])

    if not (isinstance(subject_id, int)):
        print('\nsubject_id has to be an integer')
        return
    else:
        subject_string = f'sub-{subject_id:003}'
        print(subject_string)

    if not (isinstance(session_number, int)):
        print('\nsession_number has to be an integer')
        return
    else:
        session_string = f'session-{session_number:02}'
        print(session_string)


if __name__ == '__main__':
    main()