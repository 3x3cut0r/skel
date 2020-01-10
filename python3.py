#!/usr/bin/python3
import sys
import getopt

fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]     # Argument Liste als Array aller übergebenen Parameter
unixOptions = "ho:vV"   # Argument Liste in Kurzform und aufgerufen mit z.B.: -h
gnuOptions = ["help", "output=", "verbose", "version"]  # Argument Liste ausgeschrieben und aufgerufen mit z.B.: --help

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print (str(err))
    sys.exit(2)
    
for currentArgument, currentValue in arguments:
    if currentArgument in ("-v", "--verbose"):
        print ("Aktiviere Verbose Mode")
    elif currentArgument in ("-h", "--help"):
        print ("displaying help")
    elif currentArgument in ("-o", "--output"):
        print (("enabling special output mode (%s)") % (currentValue))
    elif currentArgument in ("-V", "--version"):
        print ("Version 1.0")

print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.BOLD + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)


def main(argv):
    # My code here
    pass

if __name__ == "__main__":
    main(sys.argv)
