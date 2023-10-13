import argparse
import sys

def parse_args():

    parser = argparse.ArgumentParser(description = 'Checking whether input consists of integers and is within reasonable range.')

    parser.add_argument('--subject_id', type = int, choices = range(0, 99), nargs = '?', help = '''Subject ID. This should be an integer between 0 and 99.''')
    parser.add_argument('--session_number', type = int, choices = range(0, 9), nargs = '?', help = '''Session number. This should be an integer between 0 and 9.''')

    args = parser.parse_args()

    if args.subject_id is None or args.session_number is None:
        parser.print_help()
    exit()

    return args


def test_function(subject_id, session_number):

    inputs = parse_args(subject_id, session_number)

    subject_string = f'sub-{subject_id:003}'
    print(subject_string)

    session_string = f'session-{session_number:02}'
    print(session_string)
    print('__main__')


if __name__ == '__main__':
    test_function()