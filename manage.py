import argparse

from ckuhl import application


# Take in command line arguments
parser = argparse.ArgumentParser(description='Manage ckuhl.com')
parser.add_argument('action',
        help='''The action to take:
        One of:
        run: run the server in production mode
        debug: run the server in debugging mode
        ''')
args = parser.parse_args()


# define various actions to take
def run_prod():
    app = application.create_app()
    app.run()

def run_debug():
    app = application.create_app(debug=True)
    app.run()


# Create a mapping of command line - functions
actions = {
        'run': run_prod,
        'debug': run_debug,
        }


# Run the desired function
actions[args.action]()

