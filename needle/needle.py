#!/usr/bin/env python
import argparse
import re
import sys

# Prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

from core.framework import cli
from core.utils.printer import Colors


# ======================================================================================================================
# Setup command completion and run the UI
# ======================================================================================================================
def launch_ui(args):
    # Setup tab completion
    try:
        import readline
    except ImportError:
        print('%s[!] Module \'readline\' not available. Tab complete disabled.%s' % (Colors.R, Colors.N))
    else:
        import rlcompleter
        if 'libedit' in readline.__doc__:
            readline.parse_and_bind('bind ^I rl_complete')
        else:
            readline.parse_and_bind('tab: complete')
            readline.set_completer_delims(re.sub('[/-]', '', readline.get_completer_delims()))
    # Instantiate the UI object
    x = cli.CLI()
    # Check for and run script session
    if args.script_file:
        x.do_resource(args.script_file)
    # Run the UI
    try: 
        x.cmdloop()
    except KeyboardInterrupt: 
        print('')
    

# ======================================================================================================================
# MAIN
# ======================================================================================================================
def main():
    description = '%%(prog)s - %s %s' % (cli.__author__, cli.__email__)
    parser = argparse.ArgumentParser(description=description, version=cli.__version__)
    parser.add_argument('-r', help='load commands from a resource file', metavar='filename', dest='script_file', action='store')
    args = parser.parse_args()
    launch_ui(args)

if __name__ == '__main__':
    main()
